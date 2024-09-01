import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_cerebras import ChatCerebras

# Initialize the LLM
chat = ChatCerebras(
    model="llama3.1-70b",
)

# Define the system and human prompts
system = "You are an expert on animals who must answer questions in a manner that a 5 year old can understand."
human = "I want to learn more about this animal: {text}"

# Create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", human)
    ]
)

# Create the chatbot function
def chatbot(query):
    response = chain.invoke({"text": query})
    return response

# Streamlit app
def app():
    st.title("AI Career Coach")

    # Create a text input for the user to enter their query
    query = st.text_input("Tell me how you like to work:")

    # If the user presses the "Send" button, call the chatbot function
    if st.button("Send"):
        response = chatbot(query)
        st.text_area("Response:", value=response, height=200)

if __name__ == "__main__":
    app()
