import tweepy
from SearchUpdateStatus import SearchUpdateStatus

def streamStatusUpdate(api, filterText):
    tweets_listener = SearchUpdateStatus(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track = filterText)