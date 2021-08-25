from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import gensim.downloader  #import error?
import requests
import string
import unidecode
import re

# List of criterias to engineer extra features for the datasets
# TODO move to parameters file
Criterias=["remote work",
             "child care",
             "flexible",
             "part-time",
             "diversity",
             "equal",
             "fair",
             "balance",
             "gender",
             "support"]

# loading a Word2Vec, other possibilities are:
# print(list(gensim.downloader.info()['models'].keys()))
def model_build(w2vec_model):
    model_wiki= gensim.downloader.load(w2vec_model)  #glove-wiki-gigaword-300
    return model_wiki

# retrieving synonyms (inspect class if not working anymore)
def synonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('section', {'class': 'css-191l5o0-ClassicContentCard e1qo4u830'})
    return [span.text.strip() for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] #check if class works

# creating dictionaries of criterias terms based on synonyms
def syn_dict_list(Criterias):
    syn_dict={}
    syn_list=[]
    model_wiki=model_build("glove-wiki-gigaword-300") # using glove-wiki-gigaword-300
    for word in Criterias:
        syn_list=synonyms(word)+[word]
        if word in model_wiki.key_to_index.keys():
            syn_list+=[x[0] for x in model_wiki.most_similar(word)]
        syn_dict[word]=[x for x in set(syn_list)]
    return syn_dict #potential TODO: return only single common root for word with similar common roon

# count occurences of criteria and related terms in descriptions
def count_sup(description, dict_list):
    count_support=len([x for x in dict_list if x in description])
    return count_support

# Cleaning function that should be imported elsewhere
def clean (text):    
    text_urless=re.sub(r"(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*", '', text)
    for punctuation in string.punctuation:
        text = text_urless.replace(punctuation, ' ') # Remove Punctuation        
        lowercased = text.lower() # Lower Case    
        unaccented_string = unidecode.unidecode(lowercased) # remove accents          
        tokenized = word_tokenize(unaccented_string) # Tokenize    
        words_only = [word for word in tokenized if word.isalpha()] # Remove numbers    
        stop_words = set(stopwords.words('english')) # Make stopword list    
        without_stopwords = [word for word in words_only if not word in stop_words] # Remove Stop Words    
    return " ".join(without_stopwords)


# Building features columns
def building_features(df):
    syn_dict=syn_dict_list(Criterias)
    df["clean_description"]=df["job_description"].apply(clean)
    for x in syn_dict.keys():
        dict_list=syn_dict[x]        
        df[f"{x}"]=df["clean_description"].apply(count_sup, args=([dict_list])) 
