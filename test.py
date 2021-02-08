from fais import twittergatherer 
twitter_username = "ChantaulMusic"
twitter_keyword = None
twitter_since = "2011-01-01"
twitter_until = "2019-08-21"
twitter_criteria = twittergatherer.create_twitter_criteria(twitter_username, twitter_keyword,twitter_since,twitter_until, 10000)
twittergatherer.get_tweets_csv(twitter_criteria, "tweetsbitch.csv")