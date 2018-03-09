import csv
from bs4 import BeautifulSoup

# make an empty array for your data
rows = []
# set foldername
foldername = 'facebook-archive'
# open messages
with open('../data/%s/html/ads.htm' % foldername) as page:
    soup = BeautifulSoup(page,  "html.parser")
    # only grab the content that is relevant to us on the page using the class named "contents"
    contents = soup.find('div', class_='contents')

    # isolate all the lists of ads
    ad_lists = contents.find_all('ul')
    # lets loop through each list
    for ad_list in ad_lists:
        # for every item in this list ...
        for item in ad_list:
            advertiser = item.find(text=True)
            category = ad_list.previous_sibling.get_text()
            if item.find("div", class_='meta'):
                metadata = item.find("div", class_='meta').get_text()
            else:
                metadata = ''

            # make a data dictionary that will
            row = { 'advertiser': advertiser,
                    'category': category,
                    'metadata': metadata}

            rows.append(row)


# make a new csv into which we will write all the rows
with open('../output/%s-all-advertisers.csv' % foldername, 'w+') as csvfile:
    # these are the header names:
    fieldnames = ['advertiser', 'category', 'metadata']
    # this creates your csv
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # this writes in the first row, which are the headers
    writer.writeheader()

    # this loops through your rows (the array you set at the beginning and have updated throughtout)
    for row in rows:
        # this takes each row and writes it into your csv
        writer.writerow(row)
