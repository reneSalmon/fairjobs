# Import Libraries
import streamlit as st
import os
import json
from groq import Groq
from google.cloud import storage
from st_files_connection import FilesConnection
#from streamlit_player import st_player

# Caching imported libraries to avoid repeated imports and speed up the app
@st.cache_resource
def get_storage_client():
    return storage.Client()

@st.cache_resource
def get_groq_client(api_key):
    os.environ["GROQ_API_KEY"] = api_key
    return Groq()

def read_file(bucket_name, blob_name):
    # Get storage client and read file content
    storage_client = get_storage_client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    with blob.open("rb") as f:
        file_content = f.read()
    return file_content

def app():
    # Set up working directory and load configuration
    working_dir = os.path.dirname(os.path.abspath(__file__))
    config_data = json.load(open(f"{working_dir}/config.json"))
    GROQ_API_KEY = config_data["GROQ_API_KEY"]

    # Initialize Groq client
    client = get_groq_client(GROQ_API_KEY)

    # Initialize chat history as Streamlit session state if not present already
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Cache video loading to avoid repeated fetching
    @st.cache_data
    def load_video():
        bucket_name = "fairjobsdata"
        blob_name = "carry.mp4"
        return read_file(bucket_name, blob_name)

    video_bytes = load_video()
    st.video(video_bytes)

    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input field for user's message:
    user_prompt = st.chat_input("Ask your career questions here ... ")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})

        # Send user's message to the LLM and get a response
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            *st.session_state.chat_history
        ]

        # Consider caching or asynchronous handling for the LLM response if possible
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        assistant_response = response.choices[0].message.content
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

        # Display LLM's response
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
