from flask import Flask, render_template, request, jsonify
from twitter_client import TwitterClient

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    api = TwitterClient()

    # calling function to get tweets
    tweets = api.get_tweets(query=request.args.get('q'), count=200)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

    # percentage of positive tweets
    positive = 100*len(ptweets)/len(tweets)

    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    # percentage of negative tweets
    negative = 100*len(ntweets)/len(tweets)

    # percentage of neutral tweets
    neutral = 100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)

    return render_template(
            'index.html',
            has_results=True,
            positive=positive,
            negative=negative,
            neutral=neutral
    )

if __name__ == "__main__":
    app.run(debug=True)
