import os
import math
from collections import defaultdict, Counter
import nltk
#from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer, WordNetLemmatizer
import pandas as pd




def preprocess(text):
    stop_words = {
        'and','is','was','a','an','the','of','in','on',
    }
    tokens = text.lower().replace('.', '').split()
    #tokens = [stemmer.stem(token) for token in tokens]
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def term_incidence(processed_docs):
    N = len(processed_docs)
    terms = sorted(set(term for doc in processed_docs for term in doc))
    term_incidence = {
        term: [1 if term in doc else 0 for doc in processed_docs]
        for term in terms
    }
    print("\nTerm Incidence Matrix:")
    for term, row in term_incidence.items():
        print(term, row)

def inverted_index(processed_docs):
    inverted_index = defaultdict(list)
    for doc_id, doc in enumerate(processed_docs):
        for term in set(doc):
            inverted_index[term].append(doc_id)
    print("\nInverted Index:")
    for term, postings in inverted_index.items():
        print(term, postings)

# def cosine_similarity(query, processed_docs):
#     query = preprocess(query)

    



if __name__ == "__main__":

    #download stopwords and wordnet
    #nltk.download('stopwords')
    #nltk.download('wordnet')
    #stop words
    #stop_words = set(stopwords.words('english'))
    #stemmer = PorterStemmer()
    #lemmatizer = WordNetLemmatizer()

    #read the documents in txt format
    documents = []
    folder = "./Docs"   

    #read the documents in csv format
    df = pd.read_csv("dataset.csv")
    documents = df["text"].tolist()
    print("\nDocuments:")
    print(documents)

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(folder + "/" + file, "r") as f:
                documents.append(f.read())

    #print(documents)
    processed_docs = [preprocess(doc) for doc in documents]

    #Term Incidence Matrix
    term_incidence(processed_docs)

    #Inverted Index
    inverted_index(processed_docs)





#Query
# information retrieval and machine learning
# football sports news
# health and research data


