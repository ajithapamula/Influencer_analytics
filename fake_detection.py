import pandas as pd
import numpy as np 

def detect_spikes (series, threshold =2.5):
    diff=series.diff().fillna(0)
    Z=((diff-diff.mean())/diff.std()+1e-6)
    return Z>threshold

def compute_face_score(has_spike,engagement):
    score=0
    if has_spike:
        score+=60
    if engagement <0.015:
        score +=40
    return min(score,100)

def run_fake_detection(path=r"C:\Users\admin\Downloads\Influencer_analytics\data\growth_data.csv"):
    df=pd.read_csv(path)
    df['engagement_rate']=(df['avg_likes']+df ['avg_comments'])/df['followers']
    def parse_list(x):
            try:
                return ast.literal_eval(srt(x))
            except:
                return []
    df["growth_list"]=df ["follower_growth_last_30_days"].apply (parse_list)
    df['spike']=detect_spikes(df['followers'])
    df['fake_score']=df.apply(lambda r:compute_face_score(r['spike'],r['engagement_rate']),axis=1)
    df['reason']=df.apply(
    lambda r :"spike+low engagement" if(r['spike'] and r['engagement_rate']<0.015)
            else("follower spike" if (r['spike'])
            else("low engagement" if r ['engagement_rate']>0.015 else "Normal")),
            axis = 1
        )
    return df 

run_fake_detection()