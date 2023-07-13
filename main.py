import pandas as pd
import matplotlib.pyplot as plt
import textwrap
import numpy as np

df = pd.read_csv('dataset/imdb_cleared.csv')

def show_top5():
    df_sorted = df.drop_duplicates(subset=['title']).sort_values(by='rating', ascending=False).head()
    plotChart(df_sorted['rating'], 'List of Movies', 'Rating', 'Top 5 highest rating', df_sorted['title'])

def genres():
    top_genres = df['genre'].value_counts().head()
    plotChart(top_genres, 'Genres', 'Frequency of each genre', 'Top 5 frequent genres', top_genres.index)

def plotChart(dataframe, xlabel, ylabel, title, labels=[]):
    plt.figure(num='Chart')
    x_values = np.arange(len(dataframe))
    plt.bar(x_values, dataframe, color='steelblue', width=0.3, align='center')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    for index, value in enumerate(dataframe):
        plt.text(index, value, str(value), ha='center', va='bottom')
    plt.xticks(x_values, labels, rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


genres()
show_top5()