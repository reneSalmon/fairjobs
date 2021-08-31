#app.py
import dynamic_filtering_test
import fairjobs_web
import text_annotation
import streamlit as st

PAGES = {
    "search engine": fairjobs_web,
    "text annoation": text_annotation,
    "App3": dynamic_filtering_test
}
st.sidebar.title('Agenda')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
