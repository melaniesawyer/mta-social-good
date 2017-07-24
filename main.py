from flask import Flask, jsonify, render_template
import json
import getTweets
app = Flask(__name__)

@app.route('/data')
def data():
    tweets = getTweets.search("#MTAFail")
    return tweets

@app.route('/')
def index():
    with open('data/nyc.json') as data_file:
        data = json.load(data_file)
    with open('data/tweet-volume-borough.csv') as other_data:
        tweet_volume = other_data
    return render_template("index.html", input=data, tweets=tweet_volume)
