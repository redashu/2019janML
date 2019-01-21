#!/usr/bin/python3

import  tweepy
import  sys
from  textblob  import TextBlob
topic=sys.argv[1]
consumer_key=''
consumer_sec=''
#  by using above keys  we are going to check auth handler 
auth=tweepy.OAuthHandler(consumer_key,consumer_sec)
#  here auth is token by consuker key and sec 
access_key=''
secret_key=''
#  connecting  data server  with  access and secret key  by using above token
print(dir(auth))
auth.set_access_token(access_key,secret_key)
#  connecting to twitter api with  token that is stored in auth
connected=tweepy.API(auth)

#  searching topics 
tweet=connected.search(topic,count=10)
#  converting into text
for  j  in  tweet:
	analize=TextBlob(j.text)
	check=analize.sentiment
	print(check)


