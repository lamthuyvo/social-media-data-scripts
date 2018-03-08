# Mining data from social media platforms

![zoolander](https://cloud.githubusercontent.com/assets/3769472/23493747/11c76c1a-fedc-11e6-8b61-8da18bc72779.gif)


At present, most journalists treat social sources like they would any other — individual anecdotes and single points of contact. But to do so with a handful of tweets and Instagram posts is to ignore the potential of hundreds of millions of others.

Many stories lay dormant in the vast amounts of data produced by everyday consumers. Here's a guide and tool box that may help you. What you find below are a number of scripts developed to mine data from APIs.

Slides that explain the work process can be found [here](https://docs.google.com/presentation/d/1gVPa2cnjNZI4YnLDXDkcQSMa61r8n7MiVGdzjRZEyr4/edit?usp=sharing). I'm currently in the process of writing [more thorough resources](https://docs.google.com/document/d/1gXKdILpTmwzvn5w7mj7NgN55zT668xrM1wNjCYJG3Mw/edit?usp=sharing) on the subject of social media data mining. Feel free to reach out with questions on Twitter [@lamthuyvo](https://twitter.com/lamthuyvo)!

## How to get the data

### What data you can get with the scripts

This is a growing list of scripts we've put together to make social data mining easier.

There are broadly three different ways to harvest data from the social web:
* APIs
* Personal archives
* Scraping

##### APIs
The kind of data that official channels like API data streams provide is very limited. Despite harboring warehouses of data on consumers’ behavior, social media companies only provide a sliver of it through their APIs (for Facebook, developers can only get data for public pages and groups, and for Twitter, this access is often restricted to a set number of tweets from a user’s timeline or to a set time frame for search).

Scripts and instructions related to APIs can be found in the [`01-apis`](https://github.com/lamthuyvo/social-media-data-scripts/tree/master/01-apis) directory of this repository.

##### Personal Archives
There are ways for users of social media platforms to request and download archives of their own online persona and behavior. Some services like Facebook or Twitter will allow users to download a history of the data that constitutes their posts, their messaging, or their profile photos.

Scripts and instructions related to personal archives can be found in the [`02-personal-archives`](https://github.com/lamthuyvo/social-media-data-scripts/tree/master/02-personal-archives/) directory of this repository.

##### Scraping
Last but not least, extracting social media data from the platforms through scraping is often against the terms of service. Scraping a social media platform can get users booted from a service and potentially even result in a lawsuit.

Scripts and information related to scraping can be found in the [`03-scraping`](https://github.com/lamthuyvo/social-media-data-scripts/tree/master/03-scraping/) directory of this repository.

### Setup

Below is a set of instructions you can follow to get your machine ready to run any of the Python scripts in this repository. While Python is one of the most powerful languages for data gathering and analysis, it can take a few tries to get it installed and running properly. If you're a beginner, don't despair though, these growing pains are normal and can vary from machine to machine. We promise the payoff is worth it!

#### Before you begin

1. If you don’t already have Python installed, start by getting [Python up and running](http://docs.python-guide.org/en/latest/starting/installation/). Also have `git` installed. A helpful guide to getting a brand new machine set up can be found [here](http://blog.apps.npr.org/2013/06/06/how-to-setup-a-developers-environment.html), courtesy of [NPR's Visuals Team](https://twitter.com/nprviz).
2. [You should also make sure you have](https://pip.pypa.io/en/stable/installing/) `pip`.


#### Installing all the libraries you need

1. You need to get developer oauth credentials from the social media platforms you want to tap into. Oauth credentials are _like_ an ID and password (often referred to as an app ID and secret respectively) that you create for an app or a script to access the data stream that a social media company provides. This data stream — also known as a company's Application Program Interface, or API — is often accessible using these credentials through a link (for example, this is what one of these queries could look like https://graph.facebook.com/v2.6/BuzzFeed/posts/?fields=message/&access_token=YOURID|YOURSECRET). Here's where you can get them:
Twitter: [https://apps.twitter.com/](https://apps.twitter.com/)
Facebook: [https://developers.facebook.com/](https://developers.facebook.com/)

####  Setting up your system
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
pip install beautifulsoup4
```
or
```
sudo pip install requests
sudo pip install tweepy --ignore-installed six
pip install beautifulsoup4
```

### Getting your data

Hooray! You're ready to get your data now. We have created a directory for scripts that you can use to get data from each data source.

## Further Reading
There are numerous useful resources and tools out on the web for social media data gathering. Find an incomplete list that I'll continue to update below.


### Articles
* [Data and society: Media, Technology and Society](https://points.datasociety.net/media-technology-politics-258f4cfce87c)   
* [Sockpuppets, Secessionists, and Breitbart](https://medium.com/data-for-democracy/sockpuppets-secessionists-and-breitbart-7171b1134cd5)
* [The Atlantic: How the Like Button Ruined the Internet](https://www.theatlantic.com/technology/archive/2017/03/how-the-like-button-ruined-the-internet/519795/)
* [Linguistic data analysis of 3 billion Reddit comments](https://qz.com/1056319/what-is-the-alt-right-a-linguistic-data-analysis-of-3-billion-reddit-comments-shows-a-disparate-group-that-is-quickly-uniting/)
* [Gun emoji pairings](https://www.lexicalitems.com/blog/gun-emoji-pairings)
* [How Russian & Alt-Right Twitter Accounts Worked Together to Skew the Narrative About Berkeley](https://arcdigital.media/how-russian-alt-right-twitter-accounts-worked-together-to-skew-the-narrative-about-berkeley-f03a3d04ac5d)
* [Click fraud](https://www.bloomberg.com/features/2015-click-fraud/)
* [Your data is being manipulated](https://points.datasociety.net/your-data-is-being-manipulated-a7e31a83577b)
* [Smartphone addiction dystopia](https://www.theguardian.com/technology/2017/oct/05/smartphone-addiction-silicon-valley-dystopia)

### Books
* [Delete: The Virtue of Forgetting in the Digital Age by Viktor Mayer-Schönberger](https://www.amazon.com/Delete-Virtue-Forgetting-Digital-Age/dp/0691150362)
* [Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy by Cathy O'Neil](https://www.amazon.com/Weapons-Math-Destruction-Increases-Inequality/dp/0553418815/ref=pd_sim_14_35?_encoding=UTF8&psc=1&refRID=4NBJEE7XYFHFM2F27F4W)
* [This Is Why We Can't Have Nice Things: Mapping the Relationship between Online Trolling and Mainstream Culture by Whitney Phillips](https://www.amazon.com/This-Cant-Have-Nice-Things/dp/0262529874/ref=sr_1_1?s=books&ie=UTF8&qid=1507837769&sr=1-1&keywords=why+we+can%27t+have+nice+things+whitney)
* [Dataclysm by Christian Rudder](https://www.amazon.com/Dataclysm-Identity-What-Online-Offline-Selves/dp/0385347391/ref=sr_1_1?s=books&ie=UTF8&qid=1507837671&sr=1-1&keywords=dataclysm)
* [The Filter Bubble: How the New Personalized Web Is Changing What We Read and How We Think by Eli Pariser](https://www.amazon.com/Filter-Bubble-Personalized-Changing-Think/dp/0143121235)

### Academic research
* [Realtalk about fake news](https://www.yalelawjournal.org/forum/real-talk-about-fake-news)
* [Limited individual attention and online virality of low-quality information](http://www.readcube.com/articles/10.1038/s41562-017-0132)
* [Competition among memes in a world with limited attention](http://www.readcube.com/articles/10.1038/srep00335)
* [On confirmation bias](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.130.933&rep=rep1&type=pdf)

### Technical resources
* [Mining the Social Web (O'Reilly)](http://shop.oreilly.com/product/0636920010203.do)
* [The Digital Methods Initiative (University of Amsterdam)](https://wiki.digitalmethods.net/Dmi/ToolDatabase)
* [TrackerTracker - to extract widgets, analytics and more general trackers embedded in sites](https://wiki.digitalmethods.net/Dmi/ToolTrackerTracker)
* [Netvizz - facebook data extraction tool for groups, pages and search](https://wiki.digitalmethods.net/Dmi/ToolNetvizz)
* [TCAT - tool to collect and analyze Twitter data](https://wiki.digitalmethods.net/Dmi/ToolDmiTcat)
* [Issue Crawler and Hyphe](https://wiki.digitalmethods.net/Dmi/ToolIssueCrawler) - for [hyperlink analysis](http://hyphe.medialab.sciences-po.fr/) to see relations between websites based on how they link amongst each other
