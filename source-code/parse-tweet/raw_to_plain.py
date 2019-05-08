# file name is slang.txt
data = open("slang.txt","r")

# file including all tweets
tweets = open("tweets.txt","r")

# output file with resultant plain text
output = open("plaintext.txt","w")

# making dictionary from slang.txt
dict = {}

for line in data:
    try:
      x = line.split(":")
      dict[x[0]]=x[1].replace("\n","")
    except:
      pass  
    
 # read tweets from file and convert into list   
tweets_list = []

for line in tweets:
   try: 
      tweets_list.append(line.replace("\n",""))
   except: 
      pass 

for tweet in tweets_list:
    
    # covert into lower case
    tweet = tweet.lower()
    
    # remove all special charcters from the tweets
    tweet = tweet.replace("!"," ")
    tweet = tweet.replace("@"," ")
    tweet = tweet.replace("#"," ")
    tweet = tweet.replace("$"," ")
    tweet = tweet.replace("%"," ")
    tweet = tweet.replace("^"," ")
    tweet = tweet.replace("&"," ")
    tweet = tweet.replace("*"," ")
    tweet = tweet.replace("("," ")
    tweet = tweet.replace(")"," ")
    tweet = tweet.replace("-"," ")
    tweet = tweet.replace("_"," ")
    tweet = tweet.replace("="," ")
    tweet = tweet.replace("{"," ")
    tweet = tweet.replace("}"," ")
    tweet = tweet.replace("["," ")
    tweet = tweet.replace("]"," ")
    tweet = tweet.replace("|"," ")
    tweet = tweet.replace(":"," ")
    tweet = tweet.replace(";"," ")
    tweet = tweet.replace("'"," ")
    tweet = tweet.replace("."," ")
    tweet = tweet.replace("<"," ")
    tweet = tweet.replace(">"," ")
    tweet = tweet.replace("?"," ")
    tweet = tweet.replace("~"," ")
    tweet = tweet.replace("`"," ")

    raw = tweet.split(' ')
    
    # replace slang with actual meaning
    for idx, i in enumerate(raw):     
       if dict.has_key(i):
          raw[idx]=dict[i]
         
    plaintext = " ".join(raw)
    plaintext = " ".join(plaintext.split())
    output.write(plaintext+"\n")

print "Converting Done!!!"  

# closing the files
data.close()
tweets.close()
output.close()  
