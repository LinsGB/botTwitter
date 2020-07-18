from database import dbComands

import re

def main():
    #runComand("CREATE TABLE twitter.user (id INT AUTO_INCREMENT PRIMARY KEY, twitter_id_str VARCHAR(255), name VARCHAR(255))")
    #runComand("CREATE TABLE twitter.tweet (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(600), twitter_tweet_id VARCHAR(255), responded INT)")
    #runComand("CREATE TABLE twitter.user_tweet (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, tweet_id INT, FOREIGN KEY (user_id) REFERENCES user(id), FOREIGN KEY (tweet_id) REFERENCES tweet(id))")
    #runComandCommit("INSERT INTO twitter.tweet (twitter_tweet_id, text, responded) VALUES (%s, %s, %s)", ("1", "text", 0))
    tweets = dbComands.runComandFetchall("SELECT text FROM twitter.tweet")
    map_words = {}
    p = re.compile("@|#|/")#"@|#|/|covid"
    for tweet in tweets:
        words = tweet[0].split()
        for word in words:
            if(p.search(word.lower())):
                if(word in map_words.keys()):
                    map_words[word] = map_words[word] + 1
                else:
                    map_words[word] = 1
    x = 0
    max_words = []
    while x < 10:
        all_keys        = list(map_words.keys())
        all_values      = list(map_words.values())
        max_value       = max(all_values)
        max_value_index = all_values.index(max_value)
        bigest_key      = all_keys[max_value_index]
        
        print(bigest_key," : ", max_value)
        max_words.insert(0, bigest_key)
        del map_words[bigest_key]
        x += 1

                
            

if __name__ == "__main__":
    main()