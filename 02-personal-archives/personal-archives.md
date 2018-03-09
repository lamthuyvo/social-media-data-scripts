# Personal Archives

Our digital data archives come in all shapes and forms from timelines to message threads and comments. For most consumers, the formats provided by platforms are sufficient: users can browse their twitter history on an interactive timeline or click from message thread to message thread on the HTML pages from Facebook provides.

The scripts in this directory allow you to scrape parts of your personal Facebook archive.


### Getting started

If you have followed the installation steps from the `README.md` you can skip step 2.

1. Open up your Terminal and go to the folder where you want to clone this repository of code using the `cd` bash command.
```
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
3. To receive an archive for their personal archive, any Facebook user can head to the company's [*Downloading Your Info*](https://www.facebook.com/help/131112897028467) section. They will likely be prompted to type in their password again. Once a user has requested their archive they should receive a notification via email when it's ready to download as a zipped folder. Unzip the folder and place it into the `02-personal-archives/data/` directory in the local download of this repository. Rename the folder however you like, though you should avoid spaces.

## How to run each script
1. Follow the instructions in the comments of each script to customize your API query and resulting `.csv` file
2. Run your script with the bash command `python3 scriptname.py` (unfortunately, this set of scripts has not been optimized for Python 2 yet) to generate a csv of tweets or Facebook posts. Then, go make do some journalism-ing!
