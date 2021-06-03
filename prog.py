import nltk
import numpy as np
import gensim
import os
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

def nlpPart(query):
    filedoc=[]
    count=0
    for x in os.listdir():
        if x.endswith(".txt"):
            count=count+1

    rank=[]
    names=[]
    for x in os.listdir():
        if x.endswith(".txt"):
            names.append(x)
            with open(x) as f:
                sentences=sent_tokenize(f.read())
                filedoc=sentences
            filedoc
            gen_docs=[[word.lower() for word in word_tokenize(text)] for text in filedoc]
            dictionary=gensim.corpora.Dictionary(gen_docs)
            corpus=[dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
            tf_idf=gensim.models.TfidfModel(corpus)
            sims = gensim.similarities.Similarity('./',tf_idf[corpus],num_features=len(dictionary))
            querydoc=sent_tokenize(query)
            gen_query=[[word.lower() for word in word_tokenize(text)] for text in querydoc]
            dict_query=gensim.corpora.Dictionary(gen_query)
            corpus_query=[dict_query.doc2bow(gen_quer) for gen_quer in gen_query]
            query_tf_idf=tf_idf[corpus_query]
            sum_of_sims = (np.sum(sims[query_tf_idf],dtype=np.float32))
            percent=round(float(sum_of_sims/len(filedoc)) * 100)
            rank.append(percent)
            print(f'{percent}%')
    print(rank)
    print(names)

    for i in range(0,len(rank)):
        for j in range(i+1,len(rank)):
            if rank[i]<rank[j]:
                temp=rank[i]
                temp1=names[i]
                rank[i]=rank[j]
                names[i]=names[j]
                rank[j]=temp
                names[j]=temp1
    print(rank)
    print(names)
    m=1
    for x in names:
        print(f'Rank {m}: {x}')
        m=m+1
    
    return names







