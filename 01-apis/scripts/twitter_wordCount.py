import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

from tweepy import OAuthHandler
from tweepy import API

auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = API(auth)

pyTweets = api.search(q='#python',lang='en',count=100)
rTweets = api.search(q='#rstats',lang='en',count=100)

keyword = ['artificialintelligence','ai','artificial intelligence']
pyBoolean = [True if keyword[0] in pyTweets[i].text.lower() or keyword[1] in pyTweets[i].text.lower() or keyword[2] in pyTweets[i].text.lower() else False for i in range(len(pyTweets))]
print("Percentage of #python tweets containing Artificial Intelligence: "+str(sum(pyBoolean)))

rBoolean = [True if keyword[0] in rTweets[i].text.lower() or keyword[1] in rTweets[i].text.lower() or keyword[2] in rTweets[i].text.lower() else False for i in range(len(rTweets))]
print("Percentage of #rstats tweets containing Artificial Intelligence: "+str(sum(rBoolean)))