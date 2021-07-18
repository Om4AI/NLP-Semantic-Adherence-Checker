'''
----PreprocessingX : Preprocessing functions----
Developed & Written by @Om 

'''


# Libraries & dependencies

import pandas as pd
import nltk
import os
import numpy as np
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

# Install these Dependencies:
# !pip install fuzzywuzzy
# !pip install keybert
# !pip install python-Levenshtein

import sklearn
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
from nltk import RegexpParser
from nltk import pos_tag
import pandas as pd
import re
from fuzzywuzzy import process, fuzz
from nltk.corpus import stopwords
import math
from math import exp


sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')
model = KeyBERT('distilbert-base-nli-mean-tokens')

# NLTK downloads

nltk.download("stopwords")
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# Functions
def rem_stop1(filepath):
  # List of stopwords
    stopw = stopwords.words("english")
    l1 = [')','(',',','.',';',':','/','?','{','}','[',']','&','!','@','#','$','%','^','*']
    for i in l1:stopw.append(i)

    extension =""
    for i in range(len(filepath)-1, -1,-1):
      if (filepath[i]=='.'):
        break
    for j in range(i+1, len(filepath)):
      extension+=filepath[j]
    if (extension == 'csv'):
      csv = pd.read_csv(filepath, index_col= "S.No")
    else: csv = pd.read_excel(filepath, index_col= "S.No")

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
        elif (len(s)==0): fin_corpus.append("NULL")
    return fin_corpus
  

def remove_stopwords(path):
  l1 = [')','(',',','.',';',':','/','?','{','}','[',']','&','!','@','#','$','%','^','*']
  corpus1 = rem_stop1(filepath= path)
  final_corpus = []
  for i in range(len(corpus1)):
    s1 = ""
    for j in range(len(corpus1[i])):
      if corpus1[i][j] not in l1: 
        s1 += corpus1[i][j]
    final_corpus.append(s1)
  return final_corpus


def chunk_process(corpus):
  all_processed = []
  for i in corpus:
    train_text = i
    train_text = train_text.lower()
    custom_tokenizer = PunktSentenceTokenizer(train_text)
    tokenized = custom_tokenizer.tokenize(train_text) 
    pro = chunk_process_content(tokenized)
    all_processed.append(pro)
  return all_processed


def chunk_process_content(tokenized):
  processed = []
  for i in tokenized:
    words = nltk.word_tokenize(i)
    
    # Tags the words as nouns adjectives etc. (FOS)
    tagged = nltk.pos_tag(words)
  # print(tagged)

  # Extract the required words from the corpus
  pos = ["NN","NNS","NNP","JJR","JJS","NNPS","JJ"]
  for (a,b) in tagged:
    if b in pos:
      processed.append(a)

  # print(processed)
  # t = set(processed)

  t = []
  for i in processed:
    if i not in t:  t.append(i) 
  # print(t)
  processed = t
  return processed



# PreprocessingX
def pre_processx(path):
  final_corpus = remove_stopwords(path)
  processed_list = chunk_process(final_corpus)
  final_list = []
  for i in processed_list:
    # Each list
    s = ""
    for j in i:
      s = s + j + " "
    s = s.rstrip()
    final_list.append(s)

  return final_list
