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
  t = set(processed)
  processed = list(t)
  # processed.sort()
  return processed
