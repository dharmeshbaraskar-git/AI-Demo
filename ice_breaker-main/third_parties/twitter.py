import os
import logging

import tweepy

logger = logging.getLogger("twitter")



twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_SECRET"],
)



def scrape_user_tweets(username, num_tweets=5):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """
  
    auth = tweepy.OAuthHandler(twitter_client.consumer_key, twitter_client.consumer_secret)

    auth.set_access_token(twitter_client.access_token,twitter_client.access_token_secret)
    userAPI = tweepy.API(auth)
    user=userAPI.get_user(screen_name = username)

    tweet_list = []
    
    for tweet in user:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{user.id}"
        tweet_list.append(tweet_dict)


    return  user.screen_name


# if __name__ == "__main__":
    #print(scrape_user_tweets(username="hwchase17"))
