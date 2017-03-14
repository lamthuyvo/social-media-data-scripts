#!/usr/bin/env python
# encoding: utf-8

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

# Twitter API limit handler; this helps you deal with the fact that Twitter only allows you to ping its API a set number of times
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.error.TweepError:
            print("waiting 15 minutes for Twitter to let me get more tweets ᕕ( ᐛ )ᕗ")
            time.sleep(15 * 60)

# counter for console messages
counter  = 0;

# search terms
# find a full list of conventions here: https://dev.twitter.com/rest/public/search#query-operators
username = "@nhannahjones"
tweet_id = "839474548319916032"

# Open/Create a file to append data
csvFile = open_csv_w('%s-result.csv' % username)
#Use csv Writer
csvWriter = csv.writer(csvFile)
# these are the headers of your csv
csvWriter.writerow(["id",
                    "authorname",
                    "created_at",
                    "favorites",
                    "retweets",
                    "text",
                    "in_reply_to_status_id"])

# loop to put tweets into the csv
for tweet in limit_handled(tweepy.Cursor(api.search,
                    q=username,
                    # note that Twitter only makes available a sample of tweets from the last 7 days: https://dev.twitter.com/rest/public/search
                    # point of time you want the search to start
                    since="2017-01-07",
                    # point of time you want the search to end
                    until="2017-03-10",
                    lang="en").items()):
    #Write a row to the csv file/ I use encode utf-8
    # if tweet.in_reply_to_status_id == tweet_id:
    #         print(tweet.in_reply_to_status_id)
    #         print(tweet)
    csvWriter.writerow([tweet.id_str,
                    tweet.author.screen_name,
                    tweet.created_at,
                    tweet.favorite_count,
                    tweet.retweet_count,
                    tweet.text.encode("utf-8"),
                    tweet.in_reply_to_status_id])
    # this code prints information in your console while you're getting tweets
    counter += 1
    if counter % 100 == 0:
        print("%s tweets collected" % counter)

# close the file
csvFile.close()
