# Semantic Adherence Checking using NLP Algorithms

    Repository contains code for various Natural Language Processing tasks and the TF-IDFx Algorithm developed by me.

<p align="center">
<img src="https://res.cloudinary.com/rsmglobal/image/fetch/t_default/f_auto/q_auto/https://www.rsm.global/singapore/sites/default/files/media/Publications/Our%20Expert%20Insights/rsm-tmt-nlp.jpg"></p>

## TF-IDFx Algorithm:

### Introduction -
    TF-IDF stands for Term Frequency-Inverse Document Frequency
![image](https://user-images.githubusercontent.com/70912643/148727770-7f03bfd3-810b-405c-a817-e0985af3d5d9.png)

    TF-IDF in short: 
    
    FOR A CERTAIN QUERY -The value of Term Frequency(TF) changes with respect to each document
    but the value of Inverse Document Frequency(IDF) remains the same (Each term has a fixed IDF value-across documents) 
    as it depends on the full corpus of documents.
    
    Thus for getting the similarity to a certain document: [TF(for that document) * IDF(Common to all docs)]


### Explanation:
The **TF-IDFx Algorithm** is a **modified version** of the **TF-IDF algorithm** that is used to check the similarity of the words/query to a set of documents!
