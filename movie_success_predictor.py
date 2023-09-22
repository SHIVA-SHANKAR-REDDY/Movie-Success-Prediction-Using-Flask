# handling vectors, matrix etc.
import numpy as np
import pandas as pd


import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    
    
# NLP
import re
import nltk

nltk.download("stopwords")
nltk.download("punkt")
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Pre-Processing
from sklearn.preprocessing import LabelEncoder
from mlxtend.preprocessing import TransactionEncoder

# Text Vectorization 
from sklearn.feature_extraction.text import TfidfVectorizer

# import systemcheck
import joblib
enc = joblib.load("encoder.sav")
rfc = joblib.load("rfc.hdf5")

lemm = WordNetLemmatizer()

def cleaning_lemm(sent):
    sent = sent.lower()
        
    sent = re.sub(r"([^a-z ])","",sent)
    
    word_list = word_tokenize(sent)
    
    lem_words = list(map(lemm.lemmatize,word_list))
    
    cln_word = list(filter(lambda x: x not in stopwords.words("english"),lem_words))
    
    return " ".join(cln_word)




def predictor(Director,Genre,Year,Runtime,Metascore,Description):
    Director = enc["director_encode"].transform([Director])
    # Genre = Genre.split(",")
    Genre = enc["genre_transf"].transform([Genre]).astype("int").ravel()
    Description = cleaning_lemm(Description)
    Description = enc["tf_idf"].transform([Description]).toarray().ravel()
    inputs = np.array(list(Director)+[Year,Runtime,Metascore]+list(Genre)+list(Description))
    print(inputs)
    output = rfc.predict([inputs])[0]
    classes = ["Movie will likely not be a Success, It's not easy to make a Successful Movie.","Yayy... Movie will likely be a Success"]
    return classes[int(output)]


# i = ["James Gunn","Action,Adventure,Sci-Fi",2021,130,79,"A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe."]

# print(predictor(*i))