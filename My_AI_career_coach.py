#Import Libaries
import streamlit as st
import os
import json
from groq import Groq

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

    st.title("AI career chatbot powered by LLAMA 3.1")

    #display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    #input field for user's message:
    user_prompt = st.chat_input("Ask your career coach ... ")

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
