import streamlit as st
import os
import json
from groq import Groq
from google.cloud import storage
from st_files_connection import FilesConnection
import concurrent.futures  # Import concurrent.futures for threading

# Caching imported libraries to avoid repeated imports and speed up the app
@st.cache_resource
def get_storage_client():
    return storage.Client()

@st.cache_resource
def get_groq_client(api_key):
    os.environ["GROQ_API_KEY"] = api_key
    return Groq()

# Function to read the video file using background threading
def read_file_background(bucket_name, blob_name):
    storage_client = get_storage_client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    with blob.open("rb") as f:
        file_content = f.read()
    return file_content

# Function to initiate loading video in background
def load_video_background():
    bucket_name = "fairjobsdata"
    blob_name = "carry.mp4"

    # Create a ThreadPoolExecutor to handle background loading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit the read_file_background function to the executor
        future = executor.submit(read_file_background, bucket_name, blob_name)
        # Return the result once done
        return future.result()

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

    # Load the video file in the background and show a spinner while loading
    with st.spinner("Loading video..."):
        video_bytes = load_video_background()

    # Display the video in the app
    st.video(video_bytes)

    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input field for user's message
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
