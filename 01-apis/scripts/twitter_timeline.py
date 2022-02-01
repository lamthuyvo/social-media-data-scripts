import tweepy
from utils import open_csv_w


# import authentication credentials
from secrets import TWITTER_C_KEY, TWITTER_C_SECRET, TWITTER_A_KEY, TWITTER_A_SECRET

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(TWITTER_C_KEY, TWITTER_C_SECRET)
auth.set_access_token(TWITTER_A_KEY, TWITTER_A_SECRET)
api = tweepy.API(auth)


#Returns most recent 20 status/post of user/user's friends
home_timeline = api.home_timeline()
with open_csv_w('home_timeline.txt') as f:
    for tweet in home_timeline:
        print(tweet.text,file=f)


#Returns the 20 most recent mentions, including retweets.
mentions_timeline = api.mentions_timeline()
with open_csv_w('mentions_timeline.txt') as f:
    for tweet in mentions_timeline:
        print(tweet.text,file=f)

#returns 20 most recent posts of authenticating user
my_timeline = api.user_timeline()
with open_csv_w('my_timeline.txt') as f:
    for tweet in my_timeline:
        print(tweet.text,file=f)

#return 20 most recent post of calling user_id
user_timeline = api.user_timeline(user_id=1153916176453513216)
with open_csv_w('user_timeline.txt') as f:
    for tweet in user_timeline:
        print(tweet.text,file=f)