#Import our modules or packages that we will need to scrape a website
from bs4 import BeautifulSoup
import requests
import csv
import time

# identifying yourself
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36;',
            'from': 'Your name example@domain.com'}

# make an empty array for your data
rows = []

# open the web site
urls = ["https://en.wikipedia.org/wiki/Category:Women_computer_scientists", "https://en.wikipedia.org/w/index.php?title=Category:Women_computer_scientists&pagefrom=Lin%2C+Ming+C.%0AMing+C.+Lin#mw-pages"]

def scrapeContent(url):
    print('waiting for 5 seconds!')
    time.sleep(5)
    # add headers
    page = requests.get(url, headers= headers)
    page_content = page.content
    # parse the page through the BeautifulSoup library
    soup = BeautifulSoup(page_content, "html.parser")
    content = soup.find('div', class_='mw-category')
    all_groupings = content.find_all('div', class_='mw-category-group')
    for grouping in all_groupings:
        names_list = grouping.find('ul')
        category = grouping.find('h3').get_text()
        alphabetical_names = names_list.find_all('li')
        for item in alphabetical_names:
            # get the name
            name  = item.text
            # get the link
            anchortag = item.find('a',href=True)
            link = anchortag['href']
            # get the letter
            letter_name = category
            # make a data dictionary that will be written into the csv
            row = { 'name': name,
                    'link': link,
                    'letter_name': letter_name}
            rows.append(row)


for url in urls:
    scrapeContent(url)

# make a new csv into which we will write all the rows
with open('../output/tall-women-computer-scientists.csv', 'w+') as csvfile:
    # these are the header names:
    fieldnames = ['name', 'link', 'letter_name']
    # this creates your csv
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # this writes in the first row, which are the headers
    writer.writeheader()

    # this loops through your rows (the array you set at the beginning and have updated throughtout)
    for row in rows:
        # this takes each row and writes it into your csv
        writer.writerow(row)
