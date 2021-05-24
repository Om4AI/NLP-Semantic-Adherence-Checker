# Actual TF-IDFx

def get_tfidfx(query, path):
    user_desc = model.extract_keywords(query)
    print("Extracted Words: ",user_desc,"\n\n")
    # print("Words in query: ", len(user_desc))
    df = pd.read_csv(path)
    final_corpus = pre_processx(path)
    total_avg_tfidfx = 0

    # Total sentence weights
    tot_weights = [];


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
            tf = tf_num/tf_den

            # Vector of TFs
            tfs.append(tf)
  
            # Calculate docs in which word(w) appears
            if (tf_num > 0):
                idf_den += 1
        print(w)
        print("Vector of TFs: \n",tfs)
        print("Total no. of documents appeared:",idf_den)
        print("Total appearances in full set of documents: ",total_appearances,"\n")

        # IDFx calculation:
        if (idf_den == 0):
            idfx = 0
        else:
            idfx = math.log((len(final_corpus)*idf_den))
        print("IDFx (New Defination): ",idfx)

        # Calculate the values of TF-IDFx
        # Multiply tfs & idfxs
        for t1 in range(len(tfs)):
            tfs[t1] = tfs[t1] * idfx

        # TF-IDFx & Avg & Sigmoid for each words(w)
        print("TF-IDFx values:\n",tfs,"\n")
        avg_tfidfx = sum(tfs)/len(tfs)
        print("Average of tfidfx for ",w," :", avg_tfidfx)
        sig_avg_tfidfx = 1/(1 + exp(-avg_tfidfx))
        print("Sigmoid applied tfidfx: ",sig_avg_tfidfx)
        print("\n")

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
        
        print("Full Query weights: \n", tot_weights, "\n\n\n")

    for m in range(len(final_corpus)):
      tot_weights[m] = tot_weights[m]/len(user_desc)

    # for m in range(len(final_corpus)):
    #   tot_weights[m] = 1/(1 + exp(-tot_weights[m]))


    print("\n\n\nFull Query weights for each specification: ", tot_weights)
