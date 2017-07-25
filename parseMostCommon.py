import tweepy
import json
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from collections import Counter

CONSUMER_KEY = "F5KYjfio1II7SiaqFUO5LpJxy"
CONSUMER_SECRET = "rcMpH8vbMx2TMaUUBSsZpWlvmHP7JHerPt3poaKrk4MqG1Gy1B"
ACCESS_TOKEN = "2898973021-Byv3nraXEwwgknKdy4NC153ymNJfTWiTwWe0qt0"
ACCESS_TOKEN_SECRET = "efEMBl9P64VEsBGpzLCl2clVGoj7aTnqaRpnnoakVTmkJ"
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
count_all = Counter()
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['RT', 'via', 'train', 'trains', 'subway', 'extends', 'uptown']
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticons_re.search(token) else token.lower() for token in tokens]
    return tokens

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
        terms_all = [term for term in preprocess(tweet.text) if term not in stop and not term.startswith(('#', '@', '\u', 'https'))]
        # Update the counter
        count_all.update(terms_all)
    print(count_all.most_common(10))
    return "done"
search("#mtafail")