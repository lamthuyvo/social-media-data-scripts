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
"twitter",
"realdonaldtrump"
]

# Twitter API limit handler; this helps you deal with the fact that Twitter only allows you to ping its API a set number of times
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.error.TweepError:
            print("waiting 15 minutes for Twitter to let me get more tweets ᕕ( ᐛ )ᕗ")
            time.sleep(15 * 60)


def get_friends(name):

	# open spreadsheet and add column heads
	with open_csv_w('%s_friendlist.csv' % name) as f:
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
	pass

	# friends_ids returns an array of the ids of all the people the user follows
	friend_ids = api.friends_ids(screen_name = name)

	# cycle through every id in the array of people that the user follows and gather information for each one
	for friend_id in friend_ids:
			user = api.get_user(friend_id)
			# write the csv
			with open_csv_w('%s_friendlist.csv' % name) as f:
				writer = csv.writer(f)
				writer.writerow([friend_id,
								user.screen_name.encode('utf-8'),
								user.name.encode('utf-8'),
								user.description.encode('utf-8'),
								user.followers_count,
								user.friends_count,
								user.created_at,
								user.location.encode('utf-8')
				])
				print(user.screen_name.encode('utf-8'))
			pass



# for each username run the function
for name in usernames:
	get_friends(name)
