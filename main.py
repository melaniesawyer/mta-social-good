from flask import Flask, jsonify
import getTweets
app = Flask(__name__)

@app.route('/data')
def hello_world():
    tweets = getTweets.search("#MTAFail")
    return tweets
