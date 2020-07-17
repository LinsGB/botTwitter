import tweepy

from src import consumer_key, consumer_secret, access_token, access_token_secret

class ApiGenerator():
    def __init__(self):
        self.consumer_key        = consumer_key
        self.consumer_secret     = consumer_secret
        self.access_token        = access_token
        self.access_token_secret = access_token_secret

    def createApi(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, 
            wait_on_rate_limit_notify=True)
        try:
            api.verify_credentials()
            print("API CREATED")
        except Exception as e:
            print("Exception: ")
            raise e
        return api