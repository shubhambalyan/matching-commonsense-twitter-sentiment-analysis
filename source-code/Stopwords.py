#!/usr/bin/env python
'''
  Description : Filtering Stopwords
'''
from nltk.corpus import stopwords
import library 
#Find Total Stopwords in English language
print "************************"
print "   English Stopwords"
print "************************"
stop = stopwords.words('english')
count = 0;
for i in stop:
	print i   #Uncomment this line to display all english stopwords
	count = count + 1

print "Total English Stopwords %d" %(count)
an
print
print "************************"
print "   Filtering Stopwords"
print "************************"
eng_set = set(stop)
words = library.tokens("Life is Beautiful","word")
for word in words: 
	if word not in eng_set:
		print word
