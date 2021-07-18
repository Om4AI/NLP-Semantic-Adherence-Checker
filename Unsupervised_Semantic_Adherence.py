'''
----Unsupervised Semantic Adherence----
Developed & Written by @Om 

'''

# Libraries & dependencies
from PreprocessingX import pre_processx
import pandas as pd
import nltk
import os
import numpy as np
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

# Install these Dependencies:
# pip install fuzzywuzzy
# pip install keybert
# pip install python-Levenshtein

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


# Unsupervised Algorithm:
# TF-IDFx -- Developed by @Om Mule

# Actual TF-IDFx

def get_tfidfx_pre(query, path):
    user_desc = model.extract_keywords(query)
    print("Extracted Words: ",user_desc,"\n\n")
    # print("Words in query: ", len(user_desc))
    extension =""
    for i in range(len(path)-1, -1,-1):
      if (path[i]=='.'):
        break
    for j in range(i+1, len(path)):
      extension+=path[j]
    if (extension == 'csv'):
      df = pd.read_csv(path)
    else: df = pd.read_excel(path)

    final_corpus = pre_processx(path)
    total_avg_tfidfx = 0
    tf_idfx_vals = []

    # Total sentence weights
    tot_weights = []


    for (w,b) in user_desc:
        idf_den = 0
        tfs = []
        total_appearances = 0
        for d in final_corpus:
            # print(w)
            # print(d)

            # Number of occurences of word(w) in the document (d)
            tf_num = d.count(w)
            total_appearances += tf_num

            # Total words in the document(d)
            tf_den = len(d.split())
            if (tf_den == 0):tf = 0
            else:tf = tf_num/tf_den

            # Vector of TFs
            tfs.append(tf)
  
            # Calculate docs in which word(w) appears
            if (tf_num > 0):
                idf_den += 1
        # print(w)   ..
        # print("Vector of TFs: \n",tfs)    ..
        # print("Total no. of documents appeared:",idf_den)    ..
        # print("Total appearances in full set of documents: ",total_appearances,"\n")   ..

        # IDFx calculation:
        if (idf_den == 0):
            idfx = 0
        else:
            idfx = math.log((len(final_corpus)*idf_den))
        # print("IDFx (New Defination): ",idfx)   ..

        # Calculate the values of TF-IDFx
        # Multiply tfs & idfxs
        for t1 in range(len(tfs)):
            tfs[t1] = tfs[t1] * idfx

        # TF-IDFx & Avg & Sigmoid for each words(w)
        tf_idfx_vals.append(tfs)
        # print("TF-IDFx values:\n",tfs,"\n")        ..
        avg_tfidfx = sum(tfs)/len(tfs)
        # print("Average of tfidfx for ",w," :", avg_tfidfx)       ..
        sig_avg_tfidfx = 1/(1 + exp(-avg_tfidfx))
        # print("Sigmoid applied tfidfx: ",sig_avg_tfidfx)    ..
        # print("\n")    ..
 
        # Experimental
        # total_avg_tfidfx += avg_tfidfx
        # total_avg_tfidfx = total_avg_tfidfx/len(user_desc)
        # print("\n\nFull Query tfidfx score: ", total_avg_tfidfx)
        # print("Full Query sigmoid tfidfx score: ", 1/(1 + exp(-total_avg_tfidfx)))

        if (len(tot_weights) == 0):
          for r in tfs: 
            tot_weights.append(r)
        else: 
          for l in range(len(final_corpus)): 
            tot_weights[l] = tot_weights[l] + tfs[l];
        
        # print("Full Query weights: \n", tot_weights, "\n\n\n")         ..

    for m in range(len(final_corpus)):
      tot_weights[m] = tot_weights[m]/len(user_desc)

    # for m in range(len(final_corpus)):
    #   tot_weights[m] = 1/(1 + exp(-tot_weights[m]))


    print("\n\n\nFull Query weights for each specification: ", tot_weights)
    return tot_weights


# Call this function for Unsupervised results

def get_adherence(query, path, threshold):
  extension =""
  for i in range(len(path)-1, -1,-1):
    if (path[i]=='.'):
      break
  for j in range(i+1, len(path)):
    extension+=path[j]
  if (extension == 'csv'):
    df = pd.read_csv(path, index_col='S.No')
  else: df = pd.read_excel(path, index_col='S.No')

  df['Query'] = query.lower()

  list_pre = get_tfidfx_pre(query, path)
  df['Confidence Score'] = list_pre

  adherence = []
  for i in df['Confidence Score']:
    if (i>threshold): adherence.append('Yes')
    else: adherence.append('No')

  df['Semantic Adherence'] = adherence
  return df