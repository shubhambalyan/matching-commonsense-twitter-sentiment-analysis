# -*- coding: utf-8 -*-
"""
"""
from nltk.stem import PorterStemmer
import re
def replace_url():
   url = 'Owning a pet has many benefits. Did you know that having a pet is good for your health? http://buff.ly/1db7ww1 '
   urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
   return urls
        
def process_tweet(tweet):
    #Convert all tweet words into lowercase    
    lower_case = tweet.lower()
    
    #Apply stemming using Porter Stemmer.
    '''
         Stemming is a process of removing and replacing 
         word suffixes to arrive at a common root
         form of the word
    '''
    stemmer = PorterStemmer()
    plain_text = " ".join([ stemmer.stem(kw) for kw in lower_case.split(" ")])
    
    return plain_text
    
print(process_tweet("i am interested in iphone"))
print(replace_url())
