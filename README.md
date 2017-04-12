# Mining data from social media platforms

![zoolander](https://cloud.githubusercontent.com/assets/3769472/23493747/11c76c1a-fedc-11e6-8b61-8da18bc72779.gif)


At present, most journalists treat social sources like they would any other — individual anecdotes and single points of contact. But to do so with a handful of tweets and Instagram posts is to ignore the potential of hundreds of millions of others.

Many stories lay dormant in the vast amounts of data produced by everyday consumers. Here's a guide and tool box that may help you.

## How to get the data

### What data you can get with the scripts

This is a growing list of scripts we've put together to make social data mining easier. Right now we have scripts for Twitter and Facebook.

### Setup

#### Before you begin

1. If you don’t already have Python installed, start by getting [Python up and running](http://docs.python-guide.org/en/latest/starting/installation/). Also have `git` installed. A helpful guide to getting a brand new machine set up can be found [here](http://blog.apps.npr.org/2013/06/06/how-to-setup-a-developers-environment.html), courtesy of [NPR's Visuals Team](https://twitter.com/nprviz).
2. [You should also make sure you have](https://pip.pypa.io/en/stable/installing/) `pip`.


#### Twitter and Facebook-related preparations

1. You need to get developer oauth credentials from the social media platforms you want to tap into. Oauth credentials are _like_ an ID and password (often referred to as an app ID and secret respectively) that you create for an app or a script to access the data stream that a social media company provides. This data stream — also known as a company's Application Program Interface, or API — is often accessible using these credentials through a link (for example, this is what one of these queries could look like https://graph.facebook.com/v2.6/BuzzFeed/posts/?fields=message/&access_token=YOURID|YOURSECRET). Here's where you can get them:
Twitter: [https://apps.twitter.com/](https://apps.twitter.com/)
Facebook: [https://developers.facebook.com/](https://developers.facebook.com/)

####  Setting up the scripts
1. Open up your Terminal and go to the folder where you want to clone this repository of code using the `cd` bash command.
```
git clone https://github.com/lamthuyvo/social-media-data-scripts.git
cd social-data-scripts
```
2. Then install all the dependencies, i.e. the Python libraries we are using for these scripts by running the following command:
```
pip install -r requirements.txt
```
or
```
sudo pip install -r requirements.txt
```
If you have problems with installing the dependencies through
```
pip install requests
pip install tweepy --ignore-installed six
```
or
```
sudo pip install requests
sudo pip install tweepy --ignore-installed six
```
3. Make a secrets.py file that is modeled after the `secrets.py.example` file by going into the `scripts` directory and running these bash commands
```
cd scripts
cp secrets.py.example secrets.py
```
Now you have a `secrets.py` file! 🤗 Open it up in a text editor of your choice (like Atom or Sublime Text!) and fill the credentials you created earlier. Don't forget to save it!


### Using Twitter's API

#### Scripts

* [twitter_tweet_dumper.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/twitter_tweet_dumper.py): Up to 3200 tweets from an individual account (includes tweet id, time stamp, location, text, retweet count, favorite count (though the favorite count is inaccurate for retweets), whether something was a manual retweet, how it was tweeted (Tweetdek, Android, etc.)). This script was modified from [@Yanofsky](https://gist.github.com/yanofsky/5436496)'s original script.
* [twitter_get_friends.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/twitter_get_friends.py): Twitter user bios (name, display name, bio, followers count (at time of scraping),  following count (at time of scraping), when the account was created, location given in the bio) for all the accounts that a specific user follows.
* [twitter_get_followers.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/twitter_get_followers.py): Twitter user bios (name, display name, bio, followers count (at time of scraping),  following count (at time of scraping), when the account was created, location given in the bio) for all the accounts that follow a specific user.
* [twitter_bio_info_compiler.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/twitter_bio_info_compiler.py): Twitter user bios (name, display name, bio, followers count (at time of scraping),  following count (at time of scraping), when the account was created, location given in the bio) for a list of accounts you specify
* [twitter_searcher.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/twitter_searcher.py): You can search Twitter via its search API going back 7 days and grab tweets (id, author name, timestamp when it was created, favorites (again, unreliable), retweets, text)

### Using Facebook's API

Facebook does not allow you to

#### Scripts
* [fb_get_posts_fb_group.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/fb_get_posts_fb_group.py) or [fb_get_posts_fb_group_multiple.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/fb_get_posts_fb_group_multiple.py): These scripts allow you to gather data from _public_ Facebook groups, either from just one or multiple groups. Adapted from [@minimaxir](https://github.com/minimaxir/facebook-page-post-scraper)'s scripts.
* [fb_get_posts_fb_page.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/fb_get_posts_fb_page.py) or [fb_get_posts_fb_page_multiple.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/fb_get_posts_fb_page_multiple.py): These scripts allow you to gather data from _public_ Facebook pages, either from just one or multiple pages. Adapted from [@minimaxir](https://github.com/minimaxir/facebook-page-post-scraper)'s scripts.
* [fb_get_comments_from_fb.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/fb_get_comments.py): This script allows you to get the comments from each Facebook group or page _after_ you have run the aforementioned scripts. Adapted from [@minimaxir](https://github.com/minimaxir/facebook-page-post-scraper)'s scripts.


## How to run each script
1. Follow the instructions in the comments of each script to customize your API query and resulting `.csv` file
2. Run your script with the bash command `python scriptname.py` to generate a csv of tweets or Facebook posts. Then, go make do some journalism-ing!
