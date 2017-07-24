CONSUMER_KEY = "F5KYjfio1II7SiaqFUO5LpJxy"
CONSUMER_SECRET = "rcMpH8vbMx2TMaUUBSsZpWlvmHP7JHerPt3poaKrk4MqG1Gy1B" 
ACCESS_TOKEN = "2898973021-Byv3nraXEwwgknKdy4NC153ymNJfTWiTwWe0qt0"
ACCESS_TOKEN_SECRET = "efEMBl9P64VEsBGpzLCl2clVGoj7aTnqaRpnnoakVTmkJ" 

import tweepy
import json

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def search(query):
  pageNum = 1
  json_tweets = ""
  allTweets = []
  tweets = tweepy.Cursor(api.search, query, count=100).items();
  for tweet in tweets:
      allTweets.append(tweet.text)
      json_str = json.dumps(tweet._json)
      json_tweets += json_str
  return json_tweets

search("#mtafail")
