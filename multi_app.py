import streamlit as st
import fairjobs_web
import problem_page
import Gender_text_decoder
import gender_picture_decoder
import fairjobs_web_server
import Personalizer
import streamlit.components.v1 as components

PAGES = {
    "problem": problem_page,
    #"solution": fairjobs_web,
    "solution": fairjobs_web_server,
    "technology": Gender_text_decoder,
    "team": gender_picture_decoder,
    #"personalizer": Personalizer
}
st.sidebar.title('Content')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()
