import streamlit as st
import fairjobs_web
import problem_page
import Gender_text_decoder
import gender_picture_decoder
import Personalizer
import streamlit.components.v1 as components
import AI_career_coach_v2
#import fairjobs_web_server

PAGES = {
    "problem": problem_page,
    "solution": fairjobs_web,
    "technology": Gender_text_decoder,
    "AI career coach": AI_career_coach_v2,
    #"team": gender_picture_decoder,

    #"personalizer": Personalizer
}
st.sidebar.title('Content')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()
