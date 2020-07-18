import tweepy
from src import methodsForStream, counter
import json 

class SearchStatus(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        self.counter = counter

    def on_status(self, tweet):
        
        """
        json_str = json.dumps(tweet._json)
        parsed = json.loads(json_str)
        print(json.dumps(parsed, indent=4, sort_keys=True)) """ 
        #print(tweet.retweeted_status) se tiver esse dado é RT
        tweet_id_str = tweet.id_str
        #user_id_str  = tweet.user.id_str
        #user_name    = tweet.user.screen_name
        #userTableInteration(user_id_str, user_name)
        if("RT" not in tweet.text and "pt" in tweet.lang):
            print(f"{tweet.user.name}:{tweet.text}\n\n")
            methodsForStream.tweetTableInteration(tweet_id_str, tweet.text)

    def on_error(self, status):
        print("Error detected")






