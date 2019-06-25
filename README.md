# Thesis

This GitHub repository contains the Python scripts that are used in my thesis. The following scripts are stored here:
1. delperscraper.py: scraping news articles from Delpher
2. kortetekst_TC.py: saving the first 10 million tokens of a text file
3. 1embeddings.py: constructing word2vec embeddings using gensim
4. 2alignments.py: aligning the word embeddings of different time periods
5. 3dataframe.py: reading (aligned) embeddings of both time periods and merge them into one csv file
6. 4cosinedistance.py: transforming dataframe from 3dataframe.py to dictionaries to measure cosine distance
7. bokehfigure.py: creating an interactive Bokeh figure with the most changing verbs and the amount of runs they changed in
