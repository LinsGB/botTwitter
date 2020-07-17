from database import dbComands

def main():
    #runComand("CREATE TABLE twitter.user (id INT AUTO_INCREMENT PRIMARY KEY, twitter_id_str VARCHAR(255), name VARCHAR(255))")
    #runComand("CREATE TABLE twitter.tweet (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(600), twitter_tweet_id VARCHAR(255), responded INT)")
    #runComand("CREATE TABLE twitter.user_tweet (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, tweet_id INT, FOREIGN KEY (user_id) REFERENCES user(id), FOREIGN KEY (tweet_id) REFERENCES tweet(id))")
    #runComandCommit("INSERT INTO twitter.tweet (twitter_tweet_id, text, responded) VALUES (%s, %s, %s)", ("1", "text", 0))
    print(dbComands.runComandFetchall("SELECT id from twitter.tweet WHERE twitter_tweet_id = 1")[0][0])
    

if __name__ == "__main__":
    main()