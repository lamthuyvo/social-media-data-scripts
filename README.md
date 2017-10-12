# Mining data from social media platforms

![zoolander](https://cloud.githubusercontent.com/assets/3769472/23493747/11c76c1a-fedc-11e6-8b61-8da18bc72779.gif)


At present, most journalists treat social sources like they would any other — individual anecdotes and single points of contact. But to do so with a handful of tweets and Instagram posts is to ignore the potential of hundreds of millions of others.

Many stories lay dormant in the vast amounts of data produced by everyday consumers. Here's a guide and tool box that may help you. What you find below are a number of scripts developed to mine data from APIs. 

Slides that explain the work process can be found [here](https://docs.google.com/presentation/d/1kWmjesfyj3hZ7SxxXc7ZkSNn0w9eOuSxdIsywed6THI/edit?usp=sharing). I'm currently in the process of writing [more thorough resources](https://docs.google.com/document/d/1gXKdILpTmwzvn5w7mj7NgN55zT668xrM1wNjCYJG3Mw/edit?usp=sharing) on the subject of social media data mining. Feel free to reach out with questions on Twitter [@lamthuyvo](https://twitter.com/lamthuyvo)! 

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
cd social-media-data-scripts
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
* [fb_get_page_info.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/fb_get_comments.py): This script allows you to get Facebook Page information, such as the title, description, fan count, for a number of Facebook pages.  
* [fb_id_proofer.py](https://github.com/lamthuyvo/social-media-data-scripts/blob/master/scripts/fb_id_proofer.py): This script allows you to go through a list of Facebook Page IDs and see whether they are valid.


## How to run each script
1. Follow the instructions in the comments of each script to customize your API query and resulting `.csv` file
2. Run your script with the bash command `python scriptname.py` to generate a csv of tweets or Facebook posts. Then, go make do some journalism-ing!


## Further Reading
There are numerous useful resources and tools out on the web for social media data gathering. Find an incomplete list that I'll continue to update below. 

### Articles
Data and society: Media, Technology and Society <https://points.datasociety.net/media-technology-politics-258f4cfce87c>   
The Atlantic: How the Like Button Ruined the Internet  <https://www.theatlantic.com/technology/archive/2017/03/how-the-like-button-ruined-the-internet/519795/>
Linguistic data analysis of 3 billion Reddit comments:
<https://qz.com/1056319/what-is-the-alt-right-a-linguistic-data-analysis-of-3-billion-reddit-comments-shows-a-disparate-group-that-is-quickly-uniting/>
Gun emoji pairings
<https://www.lexicalitems.com/blog/gun-emoji-pairings>
How Russian & Alt-Right Twitter Accounts Worked Together to Skew the Narrative About Berkeley
<https://arcdigital.media/how-russian-alt-right-twitter-accounts-worked-together-to-skew-the-narrative-about-berkeley-f03a3d04ac5d>
Click fraud
<https://www.bloomberg.com/features/2015-click-fraud/>
Your data is being manipulated
<https://points.datasociety.net/your-data-is-being-manipulated-a7e31a83577b>
Smartphone addiction dystopia
<https://www.theguardian.com/technology/2017/oct/05/smartphone-addiction-silicon-valley-dystopia>

### Books
Delete: The Virtue of Forgetting in the Digital Age by Viktor Mayer-Schönberger
<https://www.amazon.com/Delete-Virtue-Forgetting-Digital-Age/dp/0691150362>
Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy by Cathy O'Neil
<https://www.amazon.com/Weapons-Math-Destruction-Increases-Inequality/dp/0553418815/ref=pd_sim_14_35?_encoding=UTF8&psc=1&refRID=4NBJEE7XYFHFM2F27F4W>
This Is Why We Can't Have Nice Things: Mapping the Relationship between Online Trolling and Mainstream Culture by Whitney Phillips
<https://www.amazon.com/This-Cant-Have-Nice-Things/dp/0262529874/ref=sr_1_1?s=books&ie=UTF8&qid=1507837769&sr=1-1&keywords=why+we+can%27t+have+nice+things+whitney>
Dataclysm by Christian Rudder
<https://www.amazon.com/Dataclysm-Identity-What-Online-Offline-Selves/dp/0385347391/ref=sr_1_1?s=books&ie=UTF8&qid=1507837671&sr=1-1&keywords=dataclysm>
The Filter Bubble: How the New Personalized Web Is Changing What We Read and How We Think by Eli Pariser
<https://www.amazon.com/Filter-Bubble-Personalized-Changing-Think/dp/0143121235>

### Academic research
Realtalk about fake news
<https://www.yalelawjournal.org/forum/real-talk-about-fake-news>
Limited individual attention and online virality of low-quality information
<http://www.readcube.com/articles/10.1038/s41562-017-0132>
Competition among memes in a world with limited attention
<http://www.readcube.com/articles/10.1038/srep00335>
On confirmation bias
<http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.130.933&rep=rep1&type=pdf>

### Technical resources

Mining the Social Web (O'Reilly): <http://shop.oreilly.com/product/0636920010203.do>
The Digital Methods Initiative (University of Amsterdam): <https://wiki.digitalmethods.net/Dmi/ToolDatabase>
TrackerTracker - to extract widgets, analytics and more general trackers embedded in sites
<https://wiki.digitalmethods.net/Dmi/ToolTrackerTracker>
Netvizz - facebook data extraction tool for groups, pages and search: <https://wiki.digitalmethods.net/Dmi/ToolNetvizz>
TCAT - tool to collect and analyze Twitter data:  <https://wiki.digitalmethods.net/Dmi/ToolDmiTcat>
Issue Crawler and Hyphe - for hyperlink analysis to see relations between websites based on how they link amongst each other: <https://wiki.digitalmethods.net/Dmi/ToolIssueCrawler> , <http://hyphe.medialab.sciences-po.fr/>