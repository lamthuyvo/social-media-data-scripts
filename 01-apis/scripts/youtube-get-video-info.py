import requests
import csv
import json
from utils import request_until_succeed, open_csv_w
from secrets import YOUTUBE_API_KEY

# make empty data array
rows=[]
# this is where we define the API query and all its variable
api_key = YOUTUBE_API_KEY
video_ids = ['tGRzz0oqgUE', 'JQbjS0_ZfJ0']

def get_video_data(video_id):
    # api parameters
    params = 'snippet,status,contentDetails,statistics,topicDetails,localizations'
    api_url = 'https://www.googleapis.com/youtube/v3/videos?part='+ params +'&id='+ video_id+'&key='+api_key
    # this opens the link and tells your computer that the format it is reading is JSON
    api_response = requests.get(api_url)
    videodetails = json.loads(api_response.text)
    if len(videodetails['items']) > 0:
        # Assign values from API to variables
        for item in videodetails['items']:
            youtube_id = item['id']
            publishedAt = item['snippet']['publishedAt']
            channelId = item['snippet']['channelId']
            channelTitle = item['snippet']['channelTitle']
            title = item['snippet']['localized']['title']
            description = item['snippet']['localized']['description']
            tags = ', '.join(item['snippet']['tags'])
            viewCount = item['statistics']['viewCount']
            likeCount = item['statistics']['likeCount']
            dislikeCount = item['statistics']['dislikeCount']
            favoriteCount = item['statistics']['favoriteCount']
            commentCount = item['statistics']['commentCount']
            topicCategories = ''.join(item['topicDetails']['topicCategories'])

            row = {
                    'youtube_id': youtube_id,
                    'publishedAt': publishedAt,
                    'channelId': channelId,
                    'channelTitle': channelTitle,
                    'title': title,
                    'description': description,
                    'tags': tags,
                    'viewCount': viewCount,
                    'likeCount': likeCount,
                    'dislikeCount': dislikeCount,
                    'favoriteCount': favoriteCount,
                    'commentCount': commentCount,
                    'topicCategories': topicCategories
                }

        rows.append(row)
    else:
        print(video_id + " is not a valid ID")

if __name__ == '__main__':
    for video_id in video_ids:
        get_video_data(video_id)

        # make a new csv into which we will write all the rows
    with open('../output/youtube-video-information.csv', 'w+') as csvfile:
        # these are the header names:
        fieldnames = ['youtube_id','publishedAt','channelId','channelTitle','title','description','tags','viewCount','likeCount','dislikeCount','favoriteCount','commentCount','topicCategories']
        # this creates your csv
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # this writes in the first row, which are the headers
        writer.writeheader()

        # this loops through your rows (the array you set at the beginning and have updated throughtout)
        for row in rows:
            # this takes each row and writes it into your csv
            writer.writerow(row)
