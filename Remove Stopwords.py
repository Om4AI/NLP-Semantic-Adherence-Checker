# Libraries

import pandas as pd
import numpy as np
import sklearn
import nltk
from nltk.corpus import stopwords

# List of stopwords
stopw = stopwords.words("english")
l1 = [')','(',',','.',';',':','/','?','{','}','[',']','&','!','@','#','$','%','^','*']
for i in l1:stopw.append(i)
stopw

def remove_stopwords(filepath):
    csv = pd.read_csv(filepath, index_col= "S.No")
    corpus = []
    for i in csv["Description"]:corpus.append(i.rstrip().lower())
    fin_corpus = []
    for i in range(len(corpus)):
        s = ""
        temp = corpus[i].split(" ")
        for j in range(len(temp)):
            if (temp[j] not in stopw):
                s = s + temp[j]+" "
        
        if (len(s)>1):fin_corpus.append(s.rstrip())
    return fin_corpus
  
  # Create Corpus
path = "filepath(own)"
corpus1 = remove_stopwords(filepath= path)

# Remove the slashes, hashes etc
final_corpus = []
for i in range(len(corpus1)):
    s1 = ""
    for j in range(len(corpus1[i])):
        if corpus1[i][j] not in l1: 
            s1 += corpus1[i][j]
    final_corpus.append(s1)

final_corpus
