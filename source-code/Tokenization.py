#!/usr/bin/env python
'''
  Description : Tokenization is the process of splitting 
				a string into a list of pieces, or tokens
'''
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
paragraph = "Life is very beautiful! How? It's the place where i started fresh and end up doing what I wanted. The place where I find love, family, friends, and more. The place where I turn from little to big, and young to old."
print "*******************************"
print "     Sentence Tokenizer"
print "*******************************"
sentence = sent_tokenize(paragraph)
for i in sentence:
	print i

print
print "*******************************"
print "     Word Tokenizer"
print "*******************************"
words = word_tokenize(sentence[0])
for i in words:
	print i

print
print "*******************************"
print " Regular Expression Tokenizer"
print "*******************************"
sent = "I can't say lie"
#Simple Whitesapce Tokenizer
tok = RegexpTokenizer("\s+",gaps=True)
tokens = tok.tokenize(sent)
for i in tokens:
	print i

