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
with open('../output/userinfo.csv', 'w+') as f:
		writer = csv.writer(f)
		writer.writerow(["name",
					"display_name",
					"bio",
					"followers_count",
					"following_count",
					"acct_created",
					"location"])
pass

def get_userinfo(name):
	#set user to be the screen_name
	user = api.get_user(screen_name = name)

	# create row
	userinfo = [name.encode('utf-8'),
				user.name.encode('utf-8'),
				user.description.encode('utf-8'),
				user.followers_count,
				user.friends_count,
				user.created_at,
				user.location.encode('utf-8')]
	print(userinfo)

	# write the csv
	with open_csv_w('../output/userinfo.csv') as f:
		writer = csv.writer(f)
		writer.writerows([userinfo])
	pass

# for each username run the function
for name in usernames:
	get_userinfo(name)
