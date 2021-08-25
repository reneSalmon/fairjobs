import streamlit as st
import pandas as pd
import numpy as np



'''
# fairjobs - job search engine
'''

# Search field
title = st.text_input('Enter a jobtitel or company')

# Search field
title = st.text_input('Enter where you want to work')

# Search Button
if st.button('search'):
    # print is visible in server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')

'''
personalize your search
'''

# Filter
if st.checkbox('Filter 1'):
    st.write('active')

if st.checkbox('Filter 2'):
    st.write('active')

if st.checkbox('Filter 3'):
    st.write('active')

if st.checkbox('Filter 4'):
    st.write('active')

if st.checkbox('Filter 5'):
    st.write('active')

# Display search results

#df = pd.DataFrame(np.random.randn(3, 5),
#                  columns=['Job', 'Company', 'City', 'Tone','Matching Score'])
st.write("Job search results")
df = pd.DataFrame({
    'Job':
    ['Data Scientist', 'Data Scientist', 'Data Engineer', 'Data Analyst'],
    'Company': ['Google', 'Tesla', 'Facebook', 'Volkswagen'],
    'Rating': ['4 stars', '3 stars', '5 stars', '3 stars'],
    'Tone': ['female', 'male', 'neutral', 'female'],
    'City': ['London', 'Hamburg', 'Dublin', 'Paris'],
    'Relevance Score': ['90%', '75%', '60%', '43%']
})

st.table(df.head())
