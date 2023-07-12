import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import textwrap
import numpy as np

df = pd.read_csv('dataset/imdb_cleared.csv')

def sort():
    df_sorted = df.drop_duplicates(subset=['title']).sort_values(by='rating', ascending=False)
    head_sorted = df_sorted.head()
    x_values = np.arange(len(head_sorted))
    plt.bar(x_values, head_sorted['rating'], width=0.3)
    plt.xlabel('List of Movies')
    plt.ylabel('Rating')
    plt.title('Top 5 highest rating')
    for index, value in enumerate(head_sorted['rating']):
        plt.text(x=index, y=value, s=str(value), ha='center', va='bottom')

    rotulos = [textwrap.shorten(label, width=30, placeholder="...") for label in head_sorted['title']]
    plt.xticks(x_values, rotulos, rotation=45, ha='right')
    plt.tight_layout()

    plt.show()
    
sort()