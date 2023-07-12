import pandas as pd

df = pd.read_csv('dataset/imdb_raw.csv')
df['gross'] = df['gross'].str.replace('M', '').str.replace('$', '').astype(float)
df['release_year'] = df['release_year'].str.replace('(','').str.replace(')','')
df['runtime'] = df['runtime'].str.replace(" min", '')
df.drop_duplicates('title', inplace=True)
df = df[(df['gross'] != 0.0) & (df['metascore'] != 0.0)]
df = df.assign(genre=df['genre'].str.split(', ')).explode('genre')

df.to_csv('dataset/imdb_cleared.csv')

