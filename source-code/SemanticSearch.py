'''
'''
import twitter
from nltk.corpus import wordnet as wn
#Initialize Twitter API for Public Status Search
api = twitter.Api()

#Get the Search keyword from the user
key = raw_input("Enter the keyword to Search: ")
count = raw_input("Enter the number of search results you want to retrieve: ")

#Find Alternate and Matching words of user input
synonym = []
for i in wn.synsets('love'):
	for lemma in i.lemmas:
		print lemma.name
		synonym.append(lemma.name)

#Call Search Method With Simple Query
result = api.GetSearch(term=key,per_page=count)
for i in result:
    print i.text


