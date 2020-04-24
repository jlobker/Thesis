# Thesis

This GitHub repository contains my thesis and the Python scripts that I have used in this thesis. My thesis focusses on the use of the word2vec algorithm to detect semantic change in Dutch verbs.

Abstract:

Word embedding models such as word2vec are successful as a tool to detect and discover semantic change. However, these word2vec models are unstable due to their non-deterministic nature,In this study, I trained diachronic word embeddings using SGNS on a Dutch newspaper corpus to assess known semantic changes in verbs, automatically discover semantic changes in verbs, and evaluate the stability of the model. For this, I compiled a Dutch newspaper corpus containing 100 million words per time period, extracting the data from Delpher. Sixteen word2vec models are trained five times each, with different setting for window size and dimension size, to determine the stability of each model and the influence of these two hyperparameters. This study introduces the notion of assessing the stability in diachronic word embeddings instead of in synchronic word embeddings. The outcomes of this study support the law of conformity and present that the word2vec model is indeed unstable. The hyperparameter setting of dimension size is more influencing on stability than the setting of window size.

The following scripts are stored here:
1. delperscraper.py: scraping news articles from Delpher
2. kortetekst_TC.py: saving the first 10 million tokens of a text file
3. 1embeddings.py: constructing word2vec embeddings using gensim
4. 2alignments.py: aligning the word embeddings of different time periods
5. 3dataframe.py: reading (aligned) embeddings of both time periods and merge them into one csv file
6. 4cosinedistance.py: transforming dataframe from 3dataframe.py to dictionaries to measure cosine distance
7. bokehfigure.py: creating an interactive Bokeh figure with the most changing verbs and the amount of runs they changed in
