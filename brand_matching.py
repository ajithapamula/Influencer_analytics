import numpy as np 
import pandas as pd
from sentece_transformers import sentece_transformers
from sklearn.metrics.pairwise import consine_similarity


def run_brand_matching (influencer_df,
                        brands_path="data/brands_data.csv",
                        top_k=10):
    brands=pd.read_csv(brands_path)
    model=SenteceTransformers("all-MiniLM-L6-v2")
    brands["clean_reg"]=(
        brands ["brand_description"].astype(srt)+""+
        brands ["keywords"].astype(srt).srt.replace(",",",")
    )
    top_matches={}
    for idx,brand in brand.iterrows():
        sims = sim_matrix [idx]
        top_idx=sims.argsort()[_top_k:][::-1]
        top_matches[brand["brand_id"]]=influencer_df.iloc[top_idx][["influencer_id","bio","cluster"]]
        
        return top_matches
        