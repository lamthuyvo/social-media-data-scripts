import requests
import json
import csv

# import authentication credentials
from secrets import GIPHY_API_KEY


# Set search parameters
giphy_key =
searchterm = 'computer cats'
offset = '0'
url = 'https://api.giphy.com/v1/gifs/search?api_key='+ giphy_key +'&q='+ searchterm +'&limit=25&lang=en&rating=R&offset='+ offset

# variable to hold data
rows = []

# api call to receive number of pages available
api_response = requests.get(url)
gifs = json.loads(api_response.text)

# loop that makes api call and gathers information
for count in range(0, gifs['pagination']['total_count']):
    offset = str(count)
    url = 'https://api.giphy.com/v1/gifs/search?api_key='+ giphy_key +'&q='+ searchterm +'&limit=25&lang=en&offset='+ offset
    api_response = requests.get(url)
    gifs = json.loads(api_response.text)
    # loop that goes through each gif
    for gif in gifs['data']:
        # data per gif and structuring it into key and value pairs
        row = {
            'id': gif.get('id'),
            'slug': gif['slug'],
            'username': user.get('username'),
            'display_name': user.get('display_name'),
            'is_verified': user.get('is_verified'),
            'source': gif.get('source'),
            'import_datetime': gif.get('import_datetime'),
            'trending_datetime': gif.get('trending_datetime'),
            'rating': gif.get('rating'),
            'title': gif.get('title'),
            'images_url': gif['images']['original']['url']
        }
        rows.append(row)


# make a new csv into which we will write all the rows
with open('../output/%s-giphy-metadata.csv' % searchterm, 'w+') as csvfile:
    # these are the header names:
    fieldnames = [  'id',
                    'slug',
                    'username',
                    'display_name',
                    'is_verified',
                    'source',
                    'import_datetime',
                    'trending_datetime',
                    'rating',
                    'title',
                    'images_url']
    # this creates your csv
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # this writes in the first row, which are the headers
    writer.writeheader()

    # this loops through your rows (the array you set at the beginning and have updated throughtout)
    for row in rows:
        # this takes each row and writes it into your csv
        writer.writerow(row)
