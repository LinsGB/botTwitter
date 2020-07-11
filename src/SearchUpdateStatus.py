import tweepy

class SearchUpdateStatus(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

        self.api.update_status(f"@{tweet.user.screen_name} love u baybe", in_reply_to_status_id = tweet.id, auto_populate_reply_metadata = True)


    def on_error(self, status):
        print("Error detected")

