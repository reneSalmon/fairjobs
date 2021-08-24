import streamlit as st

'''
# Fairjobs - job search engine
'''

# Search field
title = st.text_input('Enter a jobtitel or company...')

# Search Button
if st.button('search'):
    # print is visible in server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')
