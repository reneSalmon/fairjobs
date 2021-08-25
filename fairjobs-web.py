import streamlit as st
import pandas as pd
import numpy as np



'''
# fairjobs - job search engine
'''

# Search field
search_word = st.text_input('Enter a jobtitel')

# Search Button
if st.button('search'):
    # print is visible in server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')

    ### SEARCH ENGINE ###

    #Import monster job_database to access job_offers
    job_database = pd.read_csv('raw_data/monster_com-job_sample_3.csv')

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
    clean_search_word = document_test.lower()
    # Remove punctuations
    clean_search_word = re.sub(r'[%s]' % re.escape(string.punctuation), ' ',
                        clean_search_word)
    # Lowercase the numbers
    clean_search_word = re.sub(r'[0-9]', '', clean_search_word)
    # Remove the doubled space
    clean_search_word = re.sub(r'\s{2,}', ' ', clean_search_word)
    print(clean_search_word)

    # Search Function
    matched_titels = job_database['searchable_jobtitles'] == clean_search_word

    # print dataframe
    job_database[matched_titels]

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


#Create output dataframe

#Create markdown Toogle to see job describtion

#Add Css for color coding for filter words
