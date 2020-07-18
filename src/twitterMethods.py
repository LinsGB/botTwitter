import tweepy
from src.SearchStatus import SearchStatus
from src.Texts import Texts
from database import dbComands

def streamStatus(api):
    texts = Texts()
    words = texts.getWords()
    tweets_listener = SearchStatus(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track = words)

def uppdateStatus(api):
    tweet_ids = dbComands.runComandFetchall("SELECT id, twitter_tweet_id FROM twitter.tweet where responded = 0")
    if(tweet_ids != False):
        texts = Texts()
        for tweet_id in tweet_ids:
            try:
                user_screen_name = api.get_status(tweet_id[1]).user.screen_name

                api.update_status(f"oi @{user_screen_name}" + texts.getMesage() , in_reply_to_status_id = tweet_id[1], auto_populate_reply_metadata = True)
                dbComands.runComandCommit("UPDATE twitter.user_tweet SET responded = %s WHERE id = %s", (1, tweet_id[0]))
            except:
                dbComands.runComandCommit("DELETE FROM twitter.user_tweet WHERE tweet_id = %s", (tweet_id[0]))
                dbComands.runComandCommit("DELETE FROM twitter.tweet WHERE id = %s", (tweet_id[0]))

def searchTweets(api):
    texts = Texts()
    for tweet in  api.search(q = texts.words, count = 5, until = texts.date):
        print(tweet.text)
            