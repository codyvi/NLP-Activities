from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time

apikey = "xMEHDbhPoZMRBLP1ZXK4I41Dx"
apiSecretKey = "V3hEBCL2MO4gOGeVtYEQept5rtiBqVmWLU2rljYatbI39LreET"
bearerToken = "AAAAAAAAAAAAAAAAAAAAAGdxRQEAAAAAsyq%2BkwikocFP7zZJ7pkm9xF0kgE%3DQSls7CmQvKzkglQ4WhfzDPYrGJjkWuFiEbGnW2snu7k2FRlcXd"
accessToken = "1124372271685165056-xwIEZYd7KdUvuVVDeqJUiOxhahKzle"
accessSecretToken = "5M4rOWOq8Tn6qL0TS0FhsPfkmR9LyW6L8s3nkax9SknCz"

#consumer key, consumer secret, access token, access secret.
ckey="xMEHDbhPoZMRBLP1ZXK4I41Dx"
csecret="V3hEBCL2MO4gOGeVtYEQept5rtiBqVmWLU2rljYatbI39LreET"
atoken="1124372271685165056-xwIEZYd7KdUvuVVDeqJUiOxhahKzle"
asecret="5M4rOWOq8Tn6qL0TS0FhsPfkmR9LyW6L8s3nkax9SknCz"

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]

            print(tweet)
            time.sleep(0.3)

            return True
        except:
            return False

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])