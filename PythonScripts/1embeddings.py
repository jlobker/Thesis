import gensim
import argparse

'''
Script constructing word2vec embeddings using gensim, using the default parameter settings
Author: Jet Lobker
Usage: python3 1embeddings.py [inputfile]
Input file is the text file of a subcorpus
'''

parser = argparse.ArgumentParser()
parser.add_argument('input_corpus',type = str)
args = parser.parse_args()

'''
The default word2vec model is trained on the input corpus
'''
sentences = gensim.models.word2vec.LineSentence(args.input_corpus)
model = gensim.models.word2vec.Word2Vec(sg = 1, size = 100, window = 5, min_count = 100, hs = 0, negative = 5, iter = 5, sample = 10e-3)
model.build_vocab(sentences)

'''
Update the model’s neural weights from a sequence of sentences five times, to create five different embeddings per word
Write word plus embedding to text file
'''
for i in range(5):
        model.train(sentences, total_examples = model.corpus_count, epochs=model.epochs)
        model.save('{}_word2vec_modeldefault-{}.bin'.format(args.input_corpus.split('.')[0], i))

        vocab = model.wv.vocab.keys()

        with open('./{}_word2vec_embeddingsdefault-{}.txt'.format(args.input_corpus.split('.')[0], i), 'w') as f:
                #vocab length + vector size
                f.write(str(len(model.wv.vocab)))
                f.write(' 100\n')
                for word in vocab:
                        embedding_string = ' '.join([str(x) for x in model.wv[word]])
                        line = '{0} {1}\n'.format(word, embedding_string)
                        f.write(line)
