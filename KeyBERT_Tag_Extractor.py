# Libraries

import pandas as pd
# Install the dependencies
# !pip install keybert
from keybert import KeyBERT

# KeyBERT model
model = KeyBERT('distilbert-base-nli-mean-tokens')


# Tags Extractor
def KB_extract_tags(path=False, n_grams =(1,1), query=False):

  # Final tags list 
  tags = []

  # File path mentioned
  if (path):

    # Check file type
    extension =""
    for i in range(len(path)-1, -1,-1):
      if (path[i]=='.'):
        break
    for j in range(i+1, len(path)):
      extension+=path[j]
    if (extension == 'csv'):
      df = pd.read_csv(path)
    else: df = pd.read_excel(path)

    # List of all the queries from the generated DataFrame
    if ("description" in df.columns):
      queries = list(df['description'])
    elif ("Description" in df.columns): queries = list(df['Description'])
    for i in queries:
      if (len(model.extract_keywords(i,keyphrase_ngram_range=n_grams))>0):
        tags.append(model.extract_keywords(i,keyphrase_ngram_range=n_grams))
      else: 
        l = ["NULL"]
        tags.append(l)
    return tags

  # Query only 
  elif(query):
    if (len(model.extract_keywords(query,keyphrase_ngram_range=n_grams))>0):
      tags.append(model.extract_keywords(query,keyphrase_ngram_range=n_grams))
    else:
      l = ["NULL"]
      tags.append(l)
    return tags