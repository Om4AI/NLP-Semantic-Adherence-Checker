# Check if a tag needs to be removed

def check_remove(s):
  # print(s)
  l = s.split()
  for j in range(len(l)):
    l[j] = nltk.word_tokenize(l[j])
    [(a,b)] = nltk.pos_tag(l[j])
    l[j] = b
  # print(l)
  adj = l.count('JJ') + l.count('JJR') + l.count('JJS')
  adv = l.count('RB') + l.count('RBR') + l.count('RBS') 
  adjv = adj+adv
  non = l.count('NN') + l.count('NNS') + l.count('NNP') + l.count('NNPS')
  if (((adjv/len(l)) > 0.5 or (non/len(l))>= 0.6) and len(l)>2):
    return True
  else: return False
  
  
def filter_tags(tags):
  count = 0
  processed = []
  # Get each list 
  for i in range(len(tags)):
    proc_list = []
    lis = tags[i]
    # print(lis)
    # Each tuple in the list
    for j in range(len(lis)):
      tup = lis[j]
      # String to be processed
      s = tup[0] 
      if (s !='NULL'):
        if (check_remove(s)==False): proc_list.append(tup)
        else: count+=1
      else: proc_list.append(tup)
    processed.append(proc_list)
  print("Tags removed: ", count,"\n\n")
  return processed


processed = filter_tags(tags)
