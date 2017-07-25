import tweepy
import json

CONSUMER_KEY = "F5KYjfio1II7SiaqFUO5LpJxy"
CONSUMER_SECRET = "rcMpH8vbMx2TMaUUBSsZpWlvmHP7JHerPt3poaKrk4MqG1Gy1B"
ACCESS_TOKEN = "2898973021-Byv3nraXEwwgknKdy4NC153ymNJfTWiTwWe0qt0"
ACCESS_TOKEN_SECRET = "efEMBl9P64VEsBGpzLCl2clVGoj7aTnqaRpnnoakVTmkJ"
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

boroughCount = {"Manhattan":0, "Brooklyn":0, "Queens":0, "Staten Island":0, "Bronx": 0}
trainCount = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "9":0, "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "j":0, "l":0, "m":0, "n":0, "q":0, "r":0, "s":0, "t":0, "w":0, "z":0}
keyWords = []

def search(query):
    pageNum = 1
    totalCount = 0
    trainTotalCount = 0
    boroughTotalCount = 0
    json_tweets = ""
    allTweets = []
    tweetWords = []
    tweets = tweepy.Cursor(api.search, query).items();
    for tweet in tweets:
        totalCount += 1
    	# print(tweet.text)
    	tweetWords = tweet.text.split(' ')
    	for i in xrange(len(tweetWords)):
            # if tweetWords[i] == 'trains':
            #     print(tweetWords[i-3] + ' ' + tweetWords[i-2] + ' '+ tweetWords[i-1] + ' ' + tweetWords[i])
            if tweetWords[i] == 'minutes':
                print(tweetWords[i-1] + ' ' + tweetWords[i])
            if tweetWords[i] == 'station':
                print(tweetWords[i-1] + ' ' + tweetWords[i])
            if (tweetWords[i] == 'train') or (tweetWords[i] == 'trains'):
                trainTotalCount += 1
                try:
                    train = tweetWords[i-1]
                    trainCount[train.lower()] += 1
                except KeyError:
    			    print(tweetWords[i-1] + ' ' + tweetWords[i])
        if tweet.place:
            boroughTotalCount += 1
            try:
                boroughCount[tweet.place.name] += 1
            except KeyError:
                print(tweet.place.name)
        # allTweets.append(tweet.text)
        # json_str = json.dumps(tweet._json)
        # json_tweets += json_str
    #     # print(len(allTweets))
    # obj = open('tweets.json','w')
    # obj.write(json_tweets)
    # obj.close
    print(totalCount)
    print(boroughTotalCount)
    print(boroughCount)
    print(trainTotalCount)
    print(trainCount)
    return "done"
search("#mtafail")
