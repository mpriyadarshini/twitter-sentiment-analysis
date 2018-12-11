from flask import Flask, render_template, request, jsonify
from twitter_client import TwitterClient
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    api = TwitterClient()
    q = request.args.get('q')

    # calling function to get tweets
    tweets = api.get_tweets(query=q, count=200)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

    positive = round(100*len(ptweets)/len(tweets),4)

    

    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    negative = round(100*len(ntweets)/len(tweets),4)

    

    # percentage of neutral tweets 

    neutral = round(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets),4)

   

    return render_template(
            'index.html',
            has_results=True,
            positive=positive,
            negative=negative,
            neutral=neutral,
            q=q,
            ptweets=random.sample(ptweets,3),
            ntweets=random.sample(ntweets,3)
    )

if __name__ == "__main__":
    app.run(debug=True)
