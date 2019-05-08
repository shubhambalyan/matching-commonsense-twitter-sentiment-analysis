# -*- coding: utf-8 -*-
"""
"""
from nltk.stem  import PorterStemmer
from nltk.tokenize import  word_tokenize
import nltk
def process_tweet(tweet):
    stemmer = PorterStemmer()
    words = word_tokenize(tweet)
    for word in nltk.pos_tag(words):
        print(word)
    
    #print(stemmer.stem(tweet))
    
process_tweet('Stemming is funnier than a bummer says the sushi loving computer scientist')
