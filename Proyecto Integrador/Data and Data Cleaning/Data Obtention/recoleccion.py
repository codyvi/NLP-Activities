from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import TweepError

from pymongo import MongoClient


import credentials
import codecs
import json

# MONGO
class MongoAuthenticator():

    def authenticate_mongodb_client(self):
        client = MongoClient("mongodb+srv://" + credentials.MONGO_USER + ":" + credentials.MONGO_PASSWORD + "@cluster0.5oywn.mongodb.net/ProyectoFinal?retryWrites=true")
        return client

# TWITTER
class TwitterClient():
    def __init__(self):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth, wait_on_rate_limit=True)

    def get_tweets_that_mention(self, twitter_user):
        tweets = []
        done = False

        # If you want to run this program, be careful with the following line,
        # change the 'since' date to one that doesn't go beyond 7 days ago for
        # better results from Twitter's search API. max_id specifies the status id
        # of the tweet that bounds the most recent tweet to retrieve, alternatively
        # provide an 'until' date parameter and change the call to the API below
        max_id = '1419084648471306243100000'
        until = '2021-07-26'
        since = '2021-07-01'
        
        while done != True:
            cnt = 0
            query = twitter_user

            new_tweets = []
            for page in Cursor(self.twitter_client.search, q=query, count=100, max_id=max_id, since=since, until=until, result_type="recent").pages(80):
                for status in page:
                    cnt = cnt + 1
                    new_tweets.append(status)
            
            if len(new_tweets) != 12000:
                done = True
            tweets.extend(new_tweets)
            print("We found a total of %d tweets" % cnt)
            """print("Last tweet created at: %s" % str(new_tweets[-1].created_at))
            print("Last tweet has ID: %s" % str(new_tweets[-1].id))"""
            #max_id = str(new_tweets[len(new_tweets)-1].id - 1)

        print("Returning a total of %d tweets" % len(tweets))
        return tweets

# TWITTER
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
        return auth

# MAIN
if __name__ == "__main__":

    mongo_authenticator = MongoAuthenticator()
    mongo_client = mongo_authenticator.authenticate_mongodb_client()

    db = mongo_client.ProyectoFinal

    twitter_client = TwitterClient()

    typeSentiment = [
        "Negative",
        "Positive"
    ]

    #sad
    #awful
    #degrading
    #humiliation
    #happy
    sentiment = [
        "#depression",
        "#wholesome"
    ]

    i = 0
    collection = db[typeSentiment[i]]
    tweets = twitter_client.get_tweets_that_mention(sentiment[i])

    for tweet in tweets:
        try:
            doc = json.loads(json.dumps(tweet._json))
            collection.insert_one(doc)
        except BaseException as e:
            print(e)

    print("Program finished execution")