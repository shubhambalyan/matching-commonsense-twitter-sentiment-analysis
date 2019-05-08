#!/usr/bin/env python
'''
  Description : This Script will use the simple Stemming 
                technique from Python List
'''
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer

#Stemming is a technique for removing affixes from a word
my_list = ['going','cars','went','came','coming']
print "*****************************"
print "The Porter Stemmer Algorithm"
print "*****************************"
stemmer = PorterStemmer()
for i in my_list:
	print "%s => %s " %(i,stemmer.stem(i))
print

print "*******************************"
print "The Lancaster Stemmer Algorithm";
print "*******************************"
stemmer = LancasterStemmer()
for i in my_list:
	print "%s => %s " %(i,stemmer.stem(i))
print

print "*****************************"	
print "    Wornet Lemmatization"
print "*****************************"
lem = WordNetLemmatizer()
print "Cars=>%s" %lem.lemmatize('cars',pos='n')
print "Went=>%s" %lem.lemmatize('went',pos='v')
print "Coming=>%s" %lem.lemmatize('coming',pos='v')
print "Came=>%s" %lem.lemmatize('came',pos='v')
