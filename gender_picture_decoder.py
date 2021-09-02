import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# app1.py


def app():

    st.title('Gender text decoder')

    #fairjobs logo
    image = Image.open(
        './images_website/greg_presentation.png'
    )
    st.image(image)
