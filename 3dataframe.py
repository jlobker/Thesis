import numpy as np
import pandas as pd

'''
Script reading (aligned) embeddings of both time periods and merge them into one csv file
Author: Jet Lobker
Usage:  python3 3dataframe.py
        [input]       
Input is type of model, e.g. DEFAULT
'''
x = input()

for i in range(5):
    df1 = pd.read_csv('Model/Alignments_{}/{}/artikel1945-1954_shortened_word2vec_embeddings{}-{}.txt'.format(x, i, x, i), names=['woord', 'vector1945-1954'], skiprows=1)
    df1[['woord','vector1945-1954']] = df1["woord"].str.split(n=1, expand=True)

    df2 = pd.read_csv('Model/Alignments_{}/{}/artikel1985-1994_shortened_word2vec_embeddings{}-{}_aligned.txt'.format(x, i, x, i), names=['woord', 'vector1985-1994'])
    df2[['woord', 'vector1985-1994']] = df2["woord"].str.split(n=1, expand=True)

    result = pd.merge(df1, df2, how='inner', on=['woord'])
    result['vector1945-1954'] = [[float(idx) for idx in x.split()] for x in result['vector1945-1954']]
    result['vector1985-1994'] = [[float(idx) for idx in x.split()] for x in result['vector1985-1994']]
    result.sort_values(by=['woord']).to_csv('Model/Alignments_{}/{}/embeddings{}-{}.csv'.format(x, i, x, i), index=False)
