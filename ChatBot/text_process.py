import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
# things we need for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
stemmer = LancasterStemmer()

class text_process():
    """docstring for text_process."""

    def __init__(self, arg):
        super(text_process, self).__init__()
        self.arg = arg

    @staticmethod
    def entity(sentence):
        nlp = en_core_web_sm.load()
        doc = nlp(sentence)
        return doc

    @staticmethod
    # function who cleans the given sentence tokenizing+stemming
    def clean_up_sentence(sentence):

        # tokenize the pattern
        sentence_words = nltk.word_tokenize(sentence)
        # stem each word
        sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words

    @staticmethod
    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
    def bow(sentence, words, show_details=False):
        # tokenize the pattern
        sentence_words = text_process.clean_up_sentence(sentence)
        # bag of words
        bag = [0]*len(words)
        for s in sentence_words:
            for i,w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)

        return(np.array(bag))
