#!/usr/bin/env python
# encoding: utf-8
# import dependencies
import tweepy #https://github.com/tweepy/tweepy
import csv
from utils import open_csv_w
# import authentication credentials
from secrets import TWITTER_C_KEY, TWITTER_C_SECRET, TWITTER_A_KEY, TWITTER_A_SECRET

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(TWITTER_C_KEY, TWITTER_C_SECRET)
auth.set_access_token(TWITTER_A_KEY, TWITTER_A_SECRET)
api = tweepy.API(auth)



# array of user names, replace them with your own choices
usernames = [
"buzzfeed",
"buzzfeednews",
"openlab"
]


# open spreadsheet and add column heads
with open('userinfo.csv', 'w+') as f:
		writer = csv.writer(f)
		writer.writerow([
					"id",
					"screen_name",
					"display_name",
					"bio",
					"followers_count",
					"following_count",
					"favourites_count",
					"statuses_count",
					"acct_created",
					"language",
					"location",
					"is_protected",
					"is_verified"

					])
pass

def get_userinfo(name):
	#set user to be the screen_name
	user = api.get_user(screen_name = name)

	# create row
	userinfo = [user.id,
				user.screen_name,
				user.name,
				user.description,
				user.followers_count,
				user.friends_count,
				user.favourites_count,
				user.statuses_count,
				user.created_at,
				user.lang,
				user.location,
				user.protected,
				user.verified
				]
	print(userinfo)

	# write the csv
	with open_csv_w('../output/userinfo.csv') as f:
		writer = csv.writer(f)
		writer.writerows([userinfo])
	pass

# for each username run the function
for name in usernames:
	get_userinfo(name)
