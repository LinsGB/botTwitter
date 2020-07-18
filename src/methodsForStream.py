from database import dbComands
from src.Texts import Texts

def userTableInteration(user_id_str, name):
    #print("\n\nuserTableInteration:\n")
    user_id = dbComands.runComandFetchall(f"SELECT id FROM twitter.user WHERE twitter_id_str = {user_id_str}")
    if(len(user_id) == 0):
        dbComands.runComandCommit("INSERT INTO twitter.user (twitter_id_str, name) VALUES (%s, %s)", (user_id_str, name))

def tweetTableInteration(tweet_id_str, text):
    texts = Texts()
    for tex_to_compar in texts.getWords():
        if(tex_to_compar in text.lower()):
            dbComands.runComandCommit("INSERT INTO twitter.tweet (twitter_tweet_id, text, responded) VALUES (%s, %s, %s)", (tweet_id_str, text, 0))
            return


def user_tweetTableInteration(tweet_id_str, user_id_str):
    #print("\n\nuser_tweetTableInteration:\n")
    tweet_id = dbComands.runComandFetchall(f"SELECT id from twitter.tweet WHERE twitter_tweet_id = {tweet_id_str}")
    user_id  = dbComands.runComandFetchall(f"SELECT id from twitter.user WHERE twitter_id_str = {user_id_str}")
    print("tweet_id: ", tweet_id, " user_id: ", user_id)
    if(tweet_id != False and user_id != False
        and len(tweet_id) > 0 and len(user_id) > 0):
        dbComands.runComandCommit("INSERT INTO twitter.user_tweet (tweet_id, user_id) VALUES (%s, %s)", (tweet_id[0][0], user_id[0][0]))