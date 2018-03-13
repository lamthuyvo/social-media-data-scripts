import requests
import csv
import json
from utils import request_until_succeed, open_csv_w
from secrets import YOUTUBE_API_KEY

# make empty data array
rows=[]
# this is where we define the API query and all its variable
api_key = YOUTUBE_API_KEY
# add the YOUTUBE IDs into the lists here, the ID can usually be found at the end of the URL:  https://www.youtube.com/watch?v=tGRzz0oqgUE
channel_ids = ['UCJFp8uSYCjXOMnkUyb3CQ3Q', 'UC-9-kyTW8ZkZNDHQJ6FgpwQ']

def get_channel_data(channel_id):
    # api parameters
    params = 'snippet,status,contentDetails,statistics,topicDetails,localizations'
    api_url = 'https://www.googleapis.com/youtube/v3/channels?part='+ params +'&id='+ channel_id +'&key='+api_key
    # this opens the link and tells your computer that the format it is reading is JSON
    api_response = requests.get(api_url)
    channeldetails = json.loads(api_response.text)
    if len(channeldetails['items']) > 0:
        # Assign values from API to variables
        for item in channeldetails['items']:
            youtube_id = item['id']
            publishedAt = item['snippet']['publishedAt']
            title = item['snippet']['title']
            description = item['snippet']['description']
            viewCount = item['statistics']['viewCount']
            subscriberCount = item['statistics']['subscriberCount']
            videoCount = item['statistics']['videoCount']
            commentCount = item['statistics']['commentCount']

            row = {
                    'youtube_id': youtube_id,
                    'publishedAt': publishedAt,
                    'title': title,
                    'description': description,
                    'viewCount': viewCount,
                    'subscriberCount': subscriberCount,
                    'videoCount': videoCount,
                    'commentCount': commentCount
                }
        print(row)
        rows.append(row)
    else:
        print(video_id + " is not a valid ID")



if __name__ == '__main__':
    for channel_id in channel_ids:
        get_channel_data(channel_id)

    # make a new csv into which we will write all the rows
    with open('../output/youtube-channel-information.csv', 'w+') as csvfile:
            # these are the header names:
            fieldnames = ['youtube_id','publishedAt','title','description','viewCount','subscriberCount','videoCount', 'commentCount']
            # this creates your csv
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # this writes in the first row, which are the headers
            writer.writeheader()

            # this loops through your rows (the array you set at the beginning and have updated throughtout)
            for row in rows:
                # this takes each row and writes it into your csv
                writer.writerow(row)
