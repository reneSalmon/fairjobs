import streamlit as st
import fairjobs_web
import problem_page
import Gender_text_decoder
import gender_picture_decoder
import Personalizer

PAGES = {
    "problem": problem_page,
    "solution": fairjobs_web,
    "product design": Gender_text_decoder,
   # "gender picture decoder": gender_picture_decoder,
    #"personalizer": Personalizer
}
st.sidebar.title('Content')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()
