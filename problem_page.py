import streamlit as st
import pandas as pd
import numpy as np
import re
import string
import requests
from PIL import Image

# app1.py


def app():

    st.title('Problem')
    # st.markdown('''
    #     What is our topic?
    #     Why is it relevant now?
    #     Who do we want to help?
    #     What is the situation of the person?
    #     What is her problem achieving her goal?
    #     Who are we?
    #     What do we believe in?
    #     What is our vision?
    #     What is our mission?

    #     ''')



    #fairjobs logo
    image = Image.open('./images_website/problem.png')
    st.image(image)
