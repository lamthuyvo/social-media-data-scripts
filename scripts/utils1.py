import requests
import csv
import sys

def request_until_succeed(url):
    r = requests.get(url)
    success = False
    while success is False:
        try:
            if r.status_code == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)

            print("Error for URL %s: %s" % (url, datetime.datetime.now()))
            print("Retrying.")

    return r.text

# makes csv reading and writing compatible with Python 2 and 3
def open_csv_w(filename):
    """Open a csv file in proper mode depending on Python verion."""
    return(open(filename, mode='a') if sys.version_info[0] == 2 else
           open(filename, mode='a+', newline=''))

# Twitter API limit handler; this helps you deal with the fact that Twitter only allows you to ping its API a set number of times
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.error.TweepError:
            print("waiting 15 minutes for Twitter to let me get more tweets ᕕ( ᐛ )ᕗ")
            time.sleep(15 * 60)
