CONSUMER_KEY = "F5KYjfio1II7SiaqFUO5LpJxy"
CONSUMER_SECRET = "rcMpH8vbMx2TMaUUBSsZpWlvmHP7JHerPt3poaKrk4MqG1Gy1B" 
ACCESS_TOKEN = "2898973021-Byv3nraXEwwgknKdy4NC153ymNJfTWiTwWe0qt0"
ACCESS_TOKEN_SECRET = "efEMBl9P64VEsBGpzLCl2clVGoj7aTnqaRpnnoakVTmkJ" 

import tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text


search = "#MTAFail"
result = api.search(search)
for tweet in result:
	print tweet.text

search = "#MTASucks"
result = api.search(search)
for tweet in result:
	print tweet.text

search = "MTAFail"
result = api.search(search)
for tweet in result:
	print tweet.text
