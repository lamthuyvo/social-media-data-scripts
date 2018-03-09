# Scraping
Seen through the lens of a data sleuth, almost every piece of content online represents a potential trove of information to be collected. Everything is data just waiting to be structured.

Scraping is the process of automatically opening sites and gathering the data from them. This often entails looking at repetitive patterns in the HTML and CSS that contains the content we want to scrape and finding ways to gather each piece of information with your script.

Almost all social media platforms state in their terms of service that scraping their content is not allowed. It can get you booted from the service or result in a lawsuit.

Make sure you find out what policies govern your use of any given social media site.


## How do I know whether I can scrape a site?
There are two ways to find out:
1. First consult each web sites's terms of service
2. Secondly, you can also look at `robots.txt` files. They may seem a little cryptic, but you can find a handy guide to understanding them [here](http://www.robotstxt.org/robotstxt.html).

## Oh, yay, the site I want to look at allows me to scrape things!

Ok, that's great! In this directory, we've added a sample script called `wikipedia_scraper_sample.py` that allows you to scrape a list from Wikipedia (Wikipedia allows for 'benign' robots).

As with the other scripts, you can run the scripts the following way:
1. Change into the scripts directory of this folder `03-scraping/scripts/`
2. Run your script with the bash command `python3 scriptname.py` (unfortunately, this set of scripts has not been optimized for Python 2 yet) to generate a csv of the scraping results. Then, go make do some journalism-ing!

Unfortunately, every web site is structured differently and hence, every site requires a slightly different kind of scraper.

I'm developing a step-by-step walkthrough for writing a scraper is currently being developed [here](https://docs.google.com/document/d/1MlGNqXRItJFcNz9tJBK2ca0oxFMftNUrZc-PCLSvjFM/edit?usp=sharing) (this is part of a bigger [book on social media data gathering](https://docs.google.com/document/d/1gXKdILpTmwzvn5w7mj7NgN55zT668xrM1wNjCYJG3Mw/edit?usp=sharing)) but here are a few steps your scraper would have to take:
1. Open a website (whether it's through as URL or a web site you have saved locally to your computer). Some of the most common libraries used to open URLs and navigate them are [`requests`](http://docs.python-requests.org/en/master/) (Opens URLS) and [`selenium`](http://selenium-python.readthedocs.io/)
2. Read its contents. For that step many people use [`beautifulsoup4`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). To know which HTML blocks contain the kind of information you want to scrape, I'd recommend a combination of looking at the loaded page using the Chrome web inspector, copying the HTML of an
3. Write the contents to a csv

A few principles to keep in mind when you write a scraper:

1. **Polite scraping — Identify yourself at the top of your scraper**:  it’s always helpful to provide contact details to your scraper for the owner of the website we are scraping to contact us. If there are issues with our scraper the person or company owning the web site we are crawling can contact us and better understand what we are trying to do. If a website owner has the ability to contact us and tell us to adjust our scraper, we may be able to continue our work without getting booted for our efforts.
2. **Build in some timers**: Every time we open a website, we are actually trying to access information that is hosted on a server and that is then rendered in an HTML before it is interpreted in our browser. Each request requires the scripts of the website to fetch data, put it into an HTML format and transfer it to our browser. Each of these actions cost a tiny fraction of money — the same way transferring several megabytes of information on a mobile phone costs us a certain amount of money. Imagine a server having to deal with a thousand of these transfers within a second and collapsing under the speed and weight of these requests — this is what we mean by ‘overloading’ a server. In very practical ways this means that when we write a scraper or a robot, we should instruct it to ‘wait’ a few seconds between opening each website.

## But I want to scrape other social media sites
If you do want to look into scraping Twitter, there are a few resources out there that may be useful. Just proceed with caution!

* Python scripts for Twitter: https://github.com/bpb27/twitter_scraping
* Here is one way to receive data from Twitter from the tweet archivist who maintains  [trumptwitterarchive.com](http://trumptwitterarchive.com/howto/all_tweets.html)
