#!/usr/bin/env python
'''
  Description : Python Library Functions for NLTK
'''
def tokens(sentence='Please give Input',algorithm='word'):
	'''
	   Function Takes Two arguments 
	       1. Sentence to be parsed
	       2. The Algorithm or method to be used
	               2.1 Sentence Tokenize (sent)
	               2.2 Word Tokenize (word)
	               2.3 Regular Expression Tokenize(regex)
	'''
	if algorithm == 'sent':
		from nltk.tokenize import sent_tokenize
		words = sent_tokenize(sentence)		
	elif algorithm == 'word':
		from nltk.tokenize import word_tokenize
		words = word_tokenize(sentence)		
	elif algorithm == 'regex':
		from nltk.tokenize import RegexpTokenize
		tokenizer = RegexpTokenizer("\s+",gaps=True)
		words = tokenizer.tokenize(sentence)
	return words
if __name__ == '__main__':
	print tokens()

