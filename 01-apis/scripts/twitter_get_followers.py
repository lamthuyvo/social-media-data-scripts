#!/usr/bin/env python
# encoding: utf-8
# import dependencies
import tweepy #https://github.com/tweepy/tweepy
import csv
import time

from utils import open_csv_w
# import authentication credentials
from secrets import TWITTER_C_KEY, TWITTER_C_SECRET, TWITTER_A_KEY, TWITTER_A_SECRET

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(TWITTER_C_KEY, TWITTER_C_SECRET)
auth.set_access_token(TWITTER_A_KEY, TWITTER_A_SECRET)
api = tweepy.API(auth)



# array of user names, replace them with your own choices
usernames = [
"marshallproj",
"buzzfeednews"
]



def get_followers(name):

	# open spreadsheet and add column heads
	with open_csv_w('../output/%s_followerlist.csv' % name) as f:
			writer = csv.writer(f)
			writer.writerow(["id",
							"screen_name",
							"display_name",
							"bio",
							"followers_count",
							"following_count",
							"acct_created",
							"location"

			])


	# friends_ids returns an array of the ids of all the people the user follows
	follower_ids = api.followers_ids(screen_name = name)

	# cycle through every id in the array of people that the user follows and gather information for each one
	for follower_id in follower_ids:
		user = None
		while user is None:
			try:
				user = api.get_user(follower_id)
			except tweepy.error.RateLimitError:
				print("sleeping for a minute")
				time.sleep(60)

		# write the csv
		with open_csv_w('../output/%s_followerlist.csv' % name) as f:
			writer = csv.writer(f)
			writer.writerow([follower_id,
							user.screen_name.encode('utf-8'),
							user.name.encode('utf-8'),
							user.description.encode('utf-8'),
							user.followers_count,
							user.friends_count,
							user.created_at,
							user.location.encode('utf-8')
			])
			print(user.screen_name.encode('utf-8'))




# for each username run the function
for name in usernames:
	get_followers(name)
