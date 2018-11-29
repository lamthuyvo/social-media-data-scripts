import csv
from bs4 import BeautifulSoup

rows = []
foldername = 'facebook-lamthuyvo'

with open("%s/ads/advertisers_you've_interacted_with.html" % foldername) as page:
    soup = BeautifulSoup(page,  'html.parser')
    contents = soup.find('div', class_='_4t5n')
    ad_list = contents.find_all( 'div' , class_='uiBoxWhite')

    for item in ad_list:
        advert = item.find('div', class_='_2let').get_text()
        metadata = item.find('div', class_='_2lem').get_text()

        row = { 'advert': advert,
                'metadata': metadata
              }
        rows.append(row)


# make a new csv into which we will write all the rows
with open('%s-all-advertisers.csv' % foldername, 'w+') as csvfile:
    # these are the header names:
    fieldnames = ['advert', 'metadata']
    # this creates your csv
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # this writes in the first row, which are the headers
    writer.writeheader()

    # this loops through your rows (the array you set at the beginning and have updated throughtout)
    for row in rows:
        # this takes each row and writes it into your csv
        writer.writerow(row)
