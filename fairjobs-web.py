import streamlit as st
import pandas as pd
import numpy as np
import re
import string
import requests
from PIL import Image

'''
# fairjobs - job search engine
'''

#Add fairjob logo as picture
#image = Image.open('sunrise.jpg')
#st.image(image, caption='Sunrise by the mountains')

# Search field
search_word = st.text_input('Enter a jobtitel')

# Search Button
if st.button('search'):
    # print is visible in server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')

    ### SEARCH ENGINE ###

    #Import monster job_database to access job_offers
    job_database = pd.read_csv(
        'raw_data/basemodel_crit.csv'
    )

    #Clean job_title column
    job_title = job_database['job_title']

    job_title_clean = []
    for d in job_title:
        # Remove Unicode
        title_cleaning = re.sub(r'[^\x00-\x7F]+', ' ', d)
        # Remove Mentions
        title_cleaning = re.sub(r'@\w+', '', title_cleaning)
        # Lowercase the document
        title_cleaning = title_cleaning.lower()
        # Remove punctuations
        title_cleaning = re.sub(r'[%s]' % re.escape(string.punctuation), ' ',
                                title_cleaning)
        # Lowercase the numbers
        title_cleaning = re.sub(r'[0-9]', '', title_cleaning)
        # Remove the doubled space
        title_cleaning = re.sub(r'\s{2,}', ' ', title_cleaning)
        job_title_clean.append(title_cleaning)

    #Return clean job title column back to dataframe by creating new column "searchable_jobtitles"
    job_database['searchable_jobtitles'] = job_title_clean

    #Clean input 'search_word'

    # Remove Unicode
    clean_search_word = re.sub(r'[^\x00-\x7F]+', ' ', search_word)
    # Remove Mentions
    clean_search_word = re.sub(r'@\w+', '', clean_search_word)
    # Lowercase the document
    clean_search_word = clean_search_word.lower()
    # Remove punctuations
    clean_search_word = re.sub(r'[%s]' % re.escape(string.punctuation), ' ',
                        clean_search_word)
    # Lowercase the numbers
    clean_search_word = re.sub(r'[0-9]', '', clean_search_word)
    # Remove the doubled space
    clean_search_word = re.sub(r'\s{2,}', ' ', clean_search_word)
    print(clean_search_word)

    # Search function
    matched_titels = job_database['searchable_jobtitles'] == clean_search_word

    # print dataframe 1
    job_list = job_database[matched_titels]

    st.dataframe(job_list[[
        'job_title', 'gender', 'company culture', 'inclusivity',
        'family benefits', 'Personal development',
    ]])

    # print dataframe 2

    st.write("Personalize your search results")

    # Personalizer Sliderbars
    #st.beta_expander
    company_culture = st.slider('How important is the company culture to you?', 1, 10)
    inclusivity = st.slider('How important is inclusivity to you?', 1, 10)
    family_benefits = st.slider('How important are family benefits to you?', 1, 10)
    personal_development = st.slider('How important is personal development to you?', 1, 10)

    job_database["Relevance Score"]= round( 100 * (company_culture*job_database["company culture"].apply(lambda x: 1 if x=="Good" else 0) + \
                                    inclusivity*job_database["inclusivity"].apply(lambda x: 1 if x=="Good" else 0) + \
                                    family_benefits*job_database["family benefits"].apply(lambda x: 1 if x=="Good" else 0)+ \
                                    personal_development*job_database["Personal development"].apply(lambda x: 1 if x=="Good" else 0)) / (company_culture+inclusivity+family_benefits+personal_development) ,2 )

#my_expander = st.beta_expander()
#my_expander.write('Hello there!')
#clicked = my_expander.button('Click me!')

#df = pd.DataFrame({
#       'job':[job_database[matched_titels]['job_title']]
# 'Company': ['Google', 'Tesla', 'Facebook', 'Volkswagen'],
# 'Rating': ['4 stars', '3 stars', '5 stars', '3 stars'],
# 'Tone': ['female', 'male', 'neutral', 'female'],
# 'City': ['London', 'Hamburg', 'Dublin', 'Paris'],
# 'Relevance Score': ['90%', '75%', '60%', '43%']
# })
#df = pd.DataFrame(np.random.randn(3, 5),
#                  columns=['Job', 'Company', 'City', 'Tone','Matching Score'])

#st.table(df.head())


# Filter
#if st.checkbox('Filter 1'):
#    st.write('active')

#if st.checkbox('Filter 2'):
#    st.write('active')

#if st.checkbox('Filter 3'):
#    st.write('active')

#if st.checkbox('Filter 4'):
#    st.write('active')

#if st.checkbox('Filter 5'):
#    st.write('active')

# Display search results

#df = pd.DataFrame(job_database[matched_titels]),
#                  columns=['Job', 'Company', 'City', 'Tone','Matching Score'])

#Create output dataframe

#Create markdown Toogle to see job describtion

#Add Css for color coding for filter words


# or using the score directly
#job_database["Relevance Score_score"]= round( 100 * (company_culture*job_database["company culture_score"] + \
#                                  inclusivity*job_database["inclusivity_score"] + \
 #                                 family_benefits*job_database["family benefits_score"] + \
  #                                personal_development*job_database["Personal development_score"] ) \
   #                             / (company_culture+inclusivity+family_benefits+personal_development),2)
