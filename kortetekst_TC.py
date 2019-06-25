import sys
from nltk import word_tokenize, sent_tokenize
import spacy
nlp = spacy.load('nl')

"""
Script saving the first 10 million tokens of a text file
Author: Tommaso Caselli - 2018-11-01
"""

def shorttext(text):
    """

    :param text: input file per year
    :return: set of sentences - eliminates all duplicated sentences
    """
    sent = set()

    with open(text) as f:
        for line in f:
            line_stripped = line.strip()
            sentence = sent_tokenize(line_stripped)
            sentence = set(sentence)
            if len(sentence) > 0:
                for elem in sentence:
                    sent.add(elem)

    return sent



if __name__ == '__main__':

    """
    Usage: python3 kortetekst_TC.py [inputFile]
    """

    input_data = sys.argv[1]
    sentences = shorttext(input_data)

    """
    The sentences set is tokenized 
    Tokens are cleaned keeping only alphabetic characters
    Only cleaned sentences with more than 3 tokens are kept and printed to the output file
    When 10 million tokens are reached, the loop break and exit
    --> by changing the amount of tokens to be counted, you can create different subcorpora sets
    """


    counter = 0
    outputfile = input_data.split(".")[0] + "_shortened.txt"


    keep_running = True
    while (keep_running):
        output = open(outputfile, "a")
        for elem in sentences:
            tokens = [w.text.lower() for w in nlp(elem)]
            clean_tokens = [word for word in tokens if word.isalpha()]
            if len(clean_tokens) > 3:
                counter = counter + int(len(clean_tokens))
                if not counter <= 10000000:
                    keep_running = False
                    output.close()
                    break
                output.writelines(" ".join(clean_tokens) + "\n")
