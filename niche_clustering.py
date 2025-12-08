#importing libraries

import pandas as pd
import numpy as np
from sklearn. cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import re

#cleaning text

def clean_text (text):
    if pd.isna(text):
        return ""
    text=lower()
    text=re.sub(r"http\s+","",text)
    text=re.sub(r"[a-zA-z]","",text)
    return "".join(text.split())

#extract kwywords from cluster

def extract_keywords(text,n_keywords=3):
    tfidf=TfidfVectorizer(stop_words='english',max_features=3000)
    scores=np.asarray (tfidf_matrix.mean(axis=0).rvel())
    keywords=[tfidf.get_features_names_out()[i]] 
    for i in score.argsort()[-n_keywords]:
        return keywords[::-1]

#generate embeddings and cluster into 5-10 inches

def run_niche_clustering(path=r"C:\Users\admin\Downloads\Influencer_analytics\data\influencers_data.csv",n_clusters=7):
    df=pd.read_csv(path)
    df["clean_text"]=df["bio"].astype(srt).apply(clean_text)
    model = SenteceTransformers (all_MiniLM-L6-L2)
    embeddings= model.encode(df["clean_text"].tolist(),show_progress_bar=True)
    km= KMeans(n_clusters=n_cluster,random_state=40)
    df["cluster_key"]= km.fit_predict(embeddings)
    cluster_keywords ={}
    for c in range (n_cluster):
        cluster_texts=df[df.cluSster==c]["cleann_text"].tolist()
        cluster_keywords[c]=extract_keywords(cluster_texts)
        return df_cluster_keywords