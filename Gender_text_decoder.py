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
    st.title('How does fairjobs work?')
    st.write('\n')
    image = Image.open('./images_website/job_offers.png')
    st.image(image)
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.markdown("---")

    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')

    # st.title('What is the architecture?')
    # image = Image.open('./images_website/Architektur.png')
    # st.image(image)

    # st.markdown("---")

    st.title('How does the text decoder work?')
    st.write('\n')
    image = Image.open(
        './images_website/GenderDecoder.png'
    )
    st.image(image)


    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.markdown("---")
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')

    st.title('How does the personalizer work?')
    st.write('\n')
    image = Image.open('images_website/Personalizer.png')
    st.image(image)

    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.markdown("---")
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')


    # st.title('How does the picture decoder work?')
    # st.write('\n')
    # image = Image.open('./images_website/PictureClassification1.png')
    # st.image(image)


    # st.write('\n')
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')
    # st.markdown("---")
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')
    # st.write('\n')

    st.title('Team')
    st.write('\n')
    image = Image.open('./images_website/team.png')
    st.image(image)

    st.write('Grégoire Le Bras, René Salmon, Anita Fechner, Komil Nasrullaev')


    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.markdown("---")
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')


    image = Image.open('./images_website/960x0.jpg')
    st.image(image)
