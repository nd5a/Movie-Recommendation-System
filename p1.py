import pandas as pd
import numpy as np

df = pd.read_csv(r'https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Movies%20Recommendation.csv')

print(df.head())

print(df.info())

df.shape
print(df.columns)

df_features=df[['Movie_Genre', 'Movie_Keywords', 'Movie_Tagline', 'Movie_Cast', 'Movie_Director']].fillna('')

print(df_features.shape)

print(df_features)

x=df_features['Movie_Genre']+' '+df_features['Movie_Keywords']+' '+df_features['Movie_Tagline']+' '+df_features['Movie_Cast']+' '+df_features['Movie_Director']

print(x)

x.shape
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()

x=tfidf.fit_transform(x)

x.shape

print(x)

# Get feature Text Conversion to Tokens

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()

x=tfidf.fit_transform(x)

x.shape

print(x)

# Get Similarity Score Using Cosine Similarity

from sklearn.metrics.pairwise import cosine_similarity

Similarity_Score = cosine_similarity(x)

print(Similarity_Score)

Similarity_Score.shape

# Get Movie Name as input from user and validate for closest Spelling

Favourite_Movie_Name = input('Enter Your Favourite movie name : ')

All_Movies_Title_List = df['Movie_Title'].tolist()

import difflib

Movie_Recommendation = difflib.get_close_matches(Favourite_Movie_Name, All_Movies_Title_List)

Close_Match = Movie_Recommendation[0]

Index_of_Close_Match_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]
print(Index_of_Close_Match_Movie)

# Getting a list of similar movies
Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Close_Match_Movie]))
print(Recommendation_Score)

print(len(Recommendation_Score))

# Get all Movies Sort Based on Recommendation score wrt Favourite Movie

# Sorting the Movie Based on their Similarity Score

Sorted_Similar_Movies = sorted(Recommendation_Score, key=lambda x:x[1], reverse=True)

# Print the name of similar Similar Movies Based on the index

print('Top 30 Movies Suggested for You: \n')

i=1
for movie in Sorted_Similar_Movies:
    index=movie[0]
    title_from_index = df[df.index==index]['Movie_Title'].values(0)
    if i<31:
        print(i,'.',title_from_index)
        i+=1

# Top 10 Movie Recommendation System

Movie_Name = input('Enter Your Favoirate Movie Name: ')

list_of_all_titles = df['Movie_Title'].tolist()

Find_Close_Match = difflib.get_close_matches(Movie_Name, list_of_all_titles)

Close_Match = Find_Close_Match[0]

Index_of_Movie= df[df.Movie_Title == Close_Match]['Movie_ID'].values(0)

Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Movie]))

Sorted_Similar_Movies = sorted(Recommendation_Score, key=lambda x:x[1], reverse=True)

print('Top 10 Movies Suggested for You: \n')

i=1

for movie in Sorted_Similar_Movies:
    index = movie[0]
    title_from_index = df[df.Movie_ID==index]['Movie_Title'].values
    if i<11:
        print(i, '.', title_from_index)
        i+=1
