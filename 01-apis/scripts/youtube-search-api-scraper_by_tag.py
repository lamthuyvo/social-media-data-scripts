import requests
import csv
import json
from utils import request_until_succeed, open_csv_w
from secrets import YOUTUBE_API_KEY

# make empty data array
rows=[]
# this is where we define the API query and all its variable
api_key = YOUTUBE_API_KEY
# the search API caps search results to approximately 500 videos. To maximize data gathering it helps to set various start and end dates
date_strings = [
    {"start_date":"2018-01-01T00:00:00Z","end_date":"2018-06-01T00:00:00Z"},
    {"start_date":"2018-06-01T00:00:00Z","end_date":"2019-01-01T00:00:00Z"},
    {"start_date":"2019-01-01T00:00:00Z","end_date":"2019-06-01T00:00:00Z"}
]

def makeSearch(search_string):
    return search_string.replace(' ','+')

# this is where we define the API query
api_base = 'https://www.googleapis.com/youtube/v3/search?'
api_key_param = '&key=' + api_key
params = '&part=snippet&order=Viewcount&maxResults=50'
search_string = makeSearch('')
tag = '&##=' + 'AOC'
type = '&type='+ 'video'
searchterm = '&q="'+search_string +'"'
api_url = api_base+params+searchterm + tag + type + api_key_param
print(api_url)


def gatherAPIdata(start_date_string,end_date_string):
    # this opens the link and tells your computer that the format it is reading is JSON
    start_date='&publishedAfter=' + start_date_string
    end_date='&publishedBefore='+ end_date_string
    api_response = requests.get(api_url +start_date+end_date).text
    videos = json.loads(api_response)

    # this is a variable we will use to check whether there's another page from which we can get data or whether we've gotten to the end of our data query (end of the phone book!)
    has_another_page = True
    while has_another_page:
        # this is a loop, which means it takes each item in the entire json data set and cycles through it, each time print the message of the post in your console
        for video in videos['items']:
            # define each one of your rows
            publishedAt = video['snippet']['publishedAt']
            title = video['snippet']['title']
            description = video['snippet']['description']
            kind = video['id']['kind']
            videoID = video['snippet']['thumbnails']['default']['url'].replace('https://i.ytimg.com/vi/', '').replace('/default.jpg','')
            channelId = video['snippet']['channelId']
            channelTitle = video['snippet']['channelTitle']
            video_data_row  = {
                'publishedAt':publishedAt,
                'title':title,
                'description':description,
                'kind':kind,
                'videoID':videoID,
                'channelId':channelId,
                'channelTitle':channelTitle
                }
            # referring to the kinds of information you said you wanted in the query above go write a row for each facebook_post_data_row
            rows.append(video_data_row)
            # Ensure it is a post with the expected metadata
            # if there is no next page, we're done.
        if 'nextPageToken' in videos.keys():
            # the URL to the next page is given by the api output
            next_page_url = api_url + "&pageToken=" + videos['nextPageToken']
            # open the next page
            next_page_posts = requests.get(next_page_url).text
            # load the next page as a json and redefine the variable we perviously called 'posts'
            videos = json.loads(next_page_posts)
            for video in videos['items']:
                publishedAt = video['snippet']['publishedAt']
                title = video['snippet']['title']
                description = video['snippet']['description']
                kind = video['id']['kind']
                videoID = video['snippet']['thumbnails']['default']['url'].replace('https://i.ytimg.com/vi/', '').replace('/default.jpg','')
                channelId = video['snippet']['channelId']
                channelTitle = video['snippet']['channelTitle']
                video_data_row  = {
                    'publishedAt':publishedAt,
                    'title':title,
                    'description':description,
                    'kind':kind,
                    'videoID':videoID,
                    'channelId':channelId,
                    'channelTitle':channelTitle
                    }
                rows.append(video_data_row)
            # csv_writer.writerow(video_data_row)
        else:
            print('no more posts!')
            has_another_page = False


if __name__ == '__main__':
    for date_string in date_strings:
        gatherAPIdata(date_string['start_date'], date_string['end_date'])

        # make a new csv into which we will write all the rows
    with open_csv_w('../output/youtube-video-search-results.csv') as csvfile:
        # these are the header names:
        fieldnames = [
                            'publishedAt',
                            'title',
                            'description',
                            'kind',
                            'videoID',
                            'channelId',
                            'channelTitle'
                    ]
        # this creates your csv
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # this writes in the first row, which are the headers
        writer.writeheader()

        # this loops through your rows (the array you set at the beginning and have updated throughtout)
        for row in rows:
            # this takes each row and writes it into your csv
            writer.writerow(row)
