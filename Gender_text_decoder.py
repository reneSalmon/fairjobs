import streamlit as st
import pandas as pd
import numpy as np
import re
import string
import requests
from PIL import Image

# app1.py


def app():

    #st.title('product design')
    # st.markdown(
    # '''
    # Why did we do it?
    # What is it doing?
    # What did we do?
    # What was the biggest challenge?

    # ''')

    #fairjobs logo
    st.title('How does GenRank work?')
    image = Image.open(
        './images_website/GenRank_Algorithm.png'
    )
    st.image(image)
    st.title('What is the architecture?')
    image = Image.open('./images_website/Architektur.png')
    st.image(image)

    st.title('How does the text decoder work?')
    image = Image.open(
        './images_website/GenderDecoder.png'
    )
    st.image(image)

    st.title('How does the picture decoder work?')
    image = Image.open(
        './images_website/FaceDetection.png'
    )
    st.image(image)
