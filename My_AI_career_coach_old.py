#Import Libaries
import streamlit as st
import os
import json
from groq import Groq
from google.cloud import storage
from st_files_connection import FilesConnection
from streamlit_player import st_player

def app():
    #working directory
    working_dir = os.path.dirname(os.path.abspath(__file__))
    config_data = json.load(open(f"{working_dir}/config.json"))
    GROQ_API_KEY = config_data["GROQ_API_KEY"]

    #save the api key to environment variable
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY

    client = Groq()

    #Initiatlize chat history as streamlit session state if not present already
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    #Insert Youtube Video
    # st.write("Hi, I am Carry your AI Career Coach")
    # st_player("https://youtu.be/kQPSEReDux4")

    # Insert video
    def read_file(bucket_name, blob_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with blob.open("rb") as f:
            file_content = f.read()
        return file_content

    # Specify the bucket name and the file name
    bucket_name = "fairjobsdata"
    blob_name = "carry.mp4"

    # Read the file from the bucket
    video_bytes = read_file(bucket_name, blob_name)

    st.video(video_bytes)


    #display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    #input field for user's message:
    user_prompt = st.chat_input("Ask your career questions here ... ")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})

        #sens user's message to the LLM and get a response
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            *st.session_state.chat_history
        ]

        response = client.chat.completions.create(
            model ="llama-3.1-8b-instant",
            messages=messages
        )

        assistant_response = response.choices[0].message.content
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

        #display LLM's response
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
