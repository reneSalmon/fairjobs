import streamlit as st
import fairjobs_web
import problem_page
import Gender_text_decoder
import gender_picture_decoder
import Personalizer
import streamlit.components.v1 as components
import My_AI_career_coach
#import fairjobs_web_server

PAGES = {
    "problem": problem_page,
    "solution": fairjobs_web,
    "technology": Gender_text_decoder,
    "AI career coach (LLama 3.1)": My_AI_career_coach,
    #"team": gender_picture_decoder,

    #"personalizer": Personalizer
}
st.sidebar.title('Content')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()
