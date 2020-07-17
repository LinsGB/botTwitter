import tweepy
from src import methodsForStream

class SearchUpdateStatus(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}\n\n")
        #print(tweet.retweeted_status) se tiver esse dado é RT
        tweet_id_str = tweet.id_str
        #user_id_str  = tweet.user.id_str
        #user_name    = tweet.user.screen_name
        #userTableInteration(user_id_str, user_name)
        try:
            tweet.retweeted_status
            methodsForStream.tweetTableInteration(tweet_id_str, tweet.text)
        except:
            pass

    def on_error(self, status):
        print("Error detected")






