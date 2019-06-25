import pandas as pd
from ast import literal_eval
import numpy as np

'''
Script transforming dataframe from 3dataframe.py to dictionaries to measure cosine distance
Authors: Tommaso Caselli and Jet Lobker
Usage:  python3 4cosinedistance.py
        [input]       
Input is type of model, e.g. DEFAULT

with columns: woord - vector1945-1954 - vector 1985-1994
to dictionaries with woord-vector1985-1994 and woord-vector1945-1954
then measure cosine distance
'''
x = input()
for i in range(5):
    df1 = pd.read_csv('Model/Alignments_{}/{}/embeddings{}-{}.csv'.format(x, i, x, i))

    data1 = df1[['vector1945-1954']]
    data1_ = df1.loc[:,'vector1945-1954'] = df1.loc[:,'vector1945-1954'].apply(lambda x: literal_eval(x))
    array1 = data1_.values.tolist()
    token_data1 = df1[['woord']].values.tolist()
    zipped_tokens_1 = list(zip(token_data1,array1))
    final_dict_1 = {}

    for elem in zipped_tokens_1:
        final_dict_1.update(dict(zip(elem[0],np.asarray(elem[1:]))))

    data2 = df1[['vector1985-1994']]
    data2_ = df1.loc[:,'vector1985-1994'] = df1.loc[:,'vector1985-1994'].apply(lambda x: literal_eval(x))
    array2 = data2_.values.tolist()
    token_data2 = df1[['woord']].values.tolist()
    zipped_tokens_2 = list(zip(token_data2,array2))

    final_dict_2 = {}

    for elem in zipped_tokens_2:
        final_dict_2.update(dict(zip(elem[0],np.asarray(elem[1:]))))

    df2 = pd.DataFrame()
 
    for (key1, value1), (key2, value2) in zip(final_dict_1.items(), final_dict_2.items()):
        cosine_distance = 1 - np.dot(value1, value2) / (np.linalg.norm(value1) * np.linalg.norm(value2))
        temp = pd.DataFrame({'woord': [key1], 'cosine_distance {}-{}'.format(x, i): [cosine_distance]})
        df2 = pd.concat([df2, temp])

    df2.to_csv('Model/Alignments_{}/{}/cosine_distance{}-{}.csv'.format(x, i, x, i), index=False)
