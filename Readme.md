 ## Influencer Analytics & Recommendation
 ```
 It Has Three Data Sets Those Are

 1.Brands_data.csv
 2.Growth_data.csv
 3.influencers_data.csv
```
This project implements all tasks from the influencer analytics assesment

## niche classification
```
-cleaned influencer text
-generated embeddings using sentense transformers
-applied kmeans clustering
```
## fake_clustering
```
-calculate engagement rate
-parse 30 days followers growth
-detected follwers spikes using z-score anamoly detection

```
## Brand_matching
```
- combined brand description + keywords
- generated brand and influencer embeddings
-computed consise similarity
```
1 First create venv file and activate 
```
```
Python -m venv venv

ACtivated
venv/scripts/activate


## Installation
pip install -r requirements.txt

## Run Command
python niche_clustering.py
python fake_detection.py
python brand_matching.py