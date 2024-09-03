import streamlit as st
from transformers import BertTokenizer
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import math

# Download necessary NLTK data
nltk.download('punkt')

# Load the model's tokenizer
pretrained_weights = 'deepset/gbert-large'
tokenizer = BertTokenizer.from_pretrained(pretrained_weights)

# Function definition for tokenizing and print output
def tokenize_text(text):
    # Tokenize the text
    token_list = tokenizer.tokenize(text)

    # Display tokenized sentences
    st.write("Tokenized Sentences:")
    sentence_list = []
    for token in token_list:
        sentence_list.append(token)
        if token == '.':
            st.write(sentence_list)
            sentence_list = []

    # Display the number of tokens
    st.write('Die Anzahl der Tokens ist:', len(token_list))

    # Calculate Shannon entropy
    entropy = calculate_shannon_entropy(text)
    st.write(f"Shannon Entropy: {entropy:.4f}")

    # Calculate Gunning-Fog Index
    fog_index = calculate_gunning_fog_index(text)
    st.write(f"Gunning-Fog Index: {fog_index:.2f}")

    # Function to calculate Gunning-Fog Index
def calculate_gunning_fog_index(text):
    """Calculates the Gunning-Fog Index of a given text."""

    # Tokenize the text into words
    words = word_tokenize(text)

    # Count the number of sentences
    sentences = text.count('.') + text.count('?') + text.count('!')

    # Count the number of complex words (3 or more syllables)
    complex_words = 0
    for word in words:
        if len(word) >= 3 and not word.istitle():
            complex_words += 1

    # Calculate Gunning-Fog Index
    fog_index = 0.4 * ((len(words) / sentences) + (100 * complex_words / len(words)))

    return fog_index


# Function to calculate Shannon entropy
def calculate_shannon_entropy(text):
    """Calculates the Shannon entropy of a given text."""

    # Tokenize the text into words
    tokens = word_tokenize(text)

    # Calculate frequency distribution of words
    freq_dist = FreqDist(tokens)

    # Calculate probability of each word
    total_words = len(tokens)
    probabilities = [freq_dist[word] / total_words for word in freq_dist]

    # Calculate Shannon entropy
    entropy = -sum([p * math.log2(p) for p in probabilities if p > 0])

    return entropy

# Streamlit app layout
st.title('Text Tokenizer using GBERT')
st.write("Please enter text to tokenize:")

# Text input for user to enter text (initially empty)
input_text = st.text_area('Enter your text here', value='', height=200)

# Tokenize and display output when button is clicked
if st.button('Text tokenisieren'):
    if input_text.strip():  # Only tokenize if there is some input
        tokenize_text(input_text)
    else:
        st.write("Please enter some text to tokenize.")
