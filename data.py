import pandas as pd
import numpy as np
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import os

def stem(text):
    ps = PorterStemmer()
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return ' '.join(y)
def cosine_sim(a, b):
    return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
if not os.path.exists('all_titles.csv'):
    df = pd.read_csv('netflix_titles.csv')
    af = pd.read_csv('amazon_prime_titles.csv')
    dp = pd.read_csv('disney_plus_titles.csv')
    hf = pd.read_csv('hulu_titles.csv')
    df = pd.concat([df,af,dp,hf], ignore_index=True)
    df.drop_duplicates(subset='title', keep='first', inplace=True)
else:
    df = pd.read_csv('all_titles.csv')

df.drop('director', axis=1, inplace=True)
df.dropna(inplace=True)
df.reset_index()
df.drop(['rating','show_id','duration','date_added'], axis=1, inplace=True)
df.cast = df.cast.apply(lambda x: ' '.join(x.split(',')))
df.country = df.country.apply(lambda x: ' '.join(x.split(',')))
df.listed_in = df.listed_in.apply(lambda x: ' '.join(x.split(',')).lower())
df.description = df.description.apply(lambda x: ' '.join(x.split(' ')).lower())
df['tags'] = df['type'] + ' ' + df['cast'] + ' ' + df['country'] + ' ' + df['listed_in'] + ' ' + df['description'] + ' ' + df.release_year.astype(str)
df.drop(['type', 'cast', 'country', 'listed_in', 'description','release_year'], axis=1, inplace=True)
df.reset_index(drop=True, inplace=True)
df.tags = df.tags.apply(stem)
vectorizer = CountVectorizer()
vectorizer.fit(df.tags)
vector = vectorizer.transform(df.tags)
def similarities(index):
    similar = []
    for i in range(0, vector.shape[0]):
        similar.append(cosine_sim(vector[index].toarray()[0], vector[i].toarray()[0]))
    return similar
def recommend(title):
    recs = []
    index = df[df.title == title].index[0]
    similar = similarities(index)
    similar = list(enumerate(similar))
    similar = sorted(similar, key=lambda x: x[1], reverse=True)
    similar = similar[1:11]
    for i in similar:
        recs.append(df.iloc[i[0]].title)
    return recs