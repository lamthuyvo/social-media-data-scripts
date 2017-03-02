#!/usr/bin/env python
# encoding: utf-8

## Very lightly modified from David Yanofsky's
## original https://gist.github.com/yanofsky/5436496

import tweepy #https://github.com/tweepy/tweepy
import csv
from utils import open_csv_w
# import authentication credentials
from secrets import TWITTER_C_KEY, TWITTER_C_SECRET, TWITTER_A_KEY, TWITTER_A_SECRET


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(TWITTER_C_KEY, TWITTER_C_SECRET)
	auth.set_access_token(TWITTER_A_KEY, TWITTER_A_SECRET)
	api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before %s" % (oldest))

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print("...%s tweets downloaded so far" % (len(alltweets)))


	#transform the tweepy tweets into a 2D array that will populate the csv	| you can comment out data you don't need
	outtweets = [[tweet.id_str,
				tweet.created_at,
				tweet.favorite_count,
				tweet.retweet_count,
				tweet.retweeted,
				tweet.source.encode("utf-8"),
				tweet.text.encode("utf-8"),] for tweet in alltweets]

	#write the csv
	with open_csv_w('%s_tweets.csv' % screen_name) as f:
		writer = csv.writer(f)
		writer.writerow(["id",
				"created_at",
				"favorites",
				"retweets",
				"retweeted",
				"source",
				"text"])
		writer.writerows(outtweets)

	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("potus")
