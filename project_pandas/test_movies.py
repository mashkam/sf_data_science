import pandas as pd

dates = pd.read_csv('data/movies_data/dates.csv', sep=',')
movies = pd.read_csv('data/movies_data/movies.csv', sep=',')
ratings1 = pd.read_csv('data/movies_data/ratings1.csv', sep=',')
ratings2 = pd.read_csv('data/movies_data/ratings2.csv', sep=',')

dates['date'] = pd.to_datetime(dates['date'])
grouped_dates = dates.groupby(dates['date'].dt.year)
print(grouped_dates['date']
      .describe()
      .sort_values('count', ascending=False)
      .head(1))

ratings = pd.concat([ratings1, ratings2], ignore_index=True)
print(ratings)

ratings = ratings.drop_duplicates(ignore_index=True)
print(ratings.shape[0])

ratings_dates = pd.concat([ratings, dates], axis=1)
print(ratings_dates.tail(7))

joined_false = ratings_dates.join(
    movies,
    rsuffix='_right',
    how='left'
)
print(joined_false)

joined = ratings_dates.join(
    movies.set_index('movieId'),
    on='movieId',
    how='left'
)
print(joined.head())

merged = ratings_dates.merge(
    movies,
    on='movieId',
    how='left'
)
print(merged.head())

merge_ratings = ratings1.merge(ratings2, how='outer')
print(merge_ratings.shape[0])
print(merge_ratings)
