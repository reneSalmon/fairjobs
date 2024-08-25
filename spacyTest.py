import spacy
import streamlit as st

# Load the English model
nlp = spacy.load('en_core_web_sm')

text = 'This is a sample text to tokenize.'

# Tokenize the text
doc = nlp(text)

# Setup Streamlit to display tokens
st.title('SpaCy Tokenization with Streamlit')
st.write('Original Text:', text)
st.write('Tokens:')
for token in doc:
    st.write(token.text)
