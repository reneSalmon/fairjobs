import streamlit as st
from google.cloud import storage
import pandas as pd


#Number of rows to read
nrows = 100

# Function to fetch data from GCP Storage
def fetch_data(bucket_name, file_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    data = pd.read_csv(blob.open('rb'),sep=";", nrows=nrows)
    return data

# Fetching the data
bucket_name = 'fairjobsdata'
file_name = 'data_data_data_full_df_web_gd.csv'
data = fetch_data(bucket_name, file_name,)

# Display data in Streamlit
st.title('Fetched Data from Google Cloud Storage')
st.write(data)
