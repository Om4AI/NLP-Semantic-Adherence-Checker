# Libraries

import pandas as pd
import numpy as np
import sklearn
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from math import exp


def rem_stop1(filepath):
  # List of stopwords
    stopw = stopwords.words("english")
    l1 = [')','(',',','.',';',':','/','?','{','}','[',']','&','!','@','#','$','%','^','*']
    for i in l1:stopw.append(i)

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
  

def remove_stopwords(path):
  corpus1 = rem_stop1(filepath= path)
  final_corpus = []
  for i in range(len(corpus1)):
    s1 = ""
    for j in range(len(corpus1[i])):
      if corpus1[i][j] not in l1: 
        s1 += corpus1[i][j]
    final_corpus.append(s1)
  return final_corpus
