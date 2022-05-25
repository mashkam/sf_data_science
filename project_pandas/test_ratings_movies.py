import pandas as pd
import re


ratings_movies = pd.read_csv('data/ratings_movies.csv', sep=',')
print(ratings_movies)


def get_year_release(arg):
    candidates = re.findall(r'\(\d{4}\)', arg)
    if len(candidates) > 0:
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        return None


ratings_movies['year_release'] = ratings_movies['title'].apply(
    get_year_release)
print(ratings_movies['year_release'].isnull().sum())

mask = ratings_movies['year_release'] == 1999
print(ratings_movies[mask].groupby('title')['rating'].mean().sort_values())

mask1 = ratings_movies['year_release'] == 2010
print(ratings_movies[mask1].groupby('genres')['rating'].mean().sort_values())

print(ratings_movies.groupby('userId')['genres'].nunique().sort_values(
    ascending=False))

print(ratings_movies.groupby('userId')['rating'].agg(
    ['count', 'mean']
).sort_values(['count', 'mean'], ascending=[True, False]))

mask2 = ratings_movies['year_release'] == 2018
grouped = ratings_movies[mask2].groupby('genres')['rating'].agg(
    ['mean', 'count'])
print(grouped[grouped['count'] > 10].sort_values(
    by='mean',
    ascending=False))

ratings_movies['date'] = pd.to_datetime(ratings_movies['date'])
ratings_movies['year_rating'] = ratings_movies['date'].dt.year
pivot = ratings_movies.pivot_table(
    index='year_rating',
    columns='genres',
    values='rating',
    aggfunc='mean'
)
print(pivot)
