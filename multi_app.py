import streamlit as st
import fairjobs_web
import problem_page
import Gender_text_decoder
import gender_picture_decoder
import Personalizer

PAGES = {
    "problem": problem_page,
    "solution": fairjobs_web,
    "gender text decoder": Gender_text_decoder,
    "gender picture decoder": gender_picture_decoder,
    "personalizer": Personalizer
}
st.sidebar.title('Agenda')
selection = st.sidebar.radio("What's up?", list(PAGES.keys()))
page = PAGES[selection]
page.app()
