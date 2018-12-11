from flask import Flask, render_template, request

from twitter_client import TwitterClient



app = Flask(__name__)



@app.route('/')

def index():

    return render_template('index.html')



@app.route('/search')

def search():

    api = TwitterClient() 

    # calling function to get tweets 

    tweets = api.get_tweets(query=request.args.get('q'), count = 200) 



    # picking positive tweets from tweets 

    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 

    

    # percentage of positive tweets 

    positive = round(100*len(ptweets)/len(tweets),4)

    

    # picking negative tweets from tweets 

    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 

    

    # percentage of negative tweets 

    negative = round(100*len(ntweets)/len(tweets),4)

    

    # percentage of neutral tweets 

    neutral = round(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets),4)



    return render_template(

        'search.html',

        q=request.args.get('q'),

        positive=positive,

        negative=negative,

        neutral=neutral

        )



if __name__ == "__main__":

    app.run(debug=True)