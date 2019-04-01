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
video_ids = ['pwnefUaKCbc', 'JQbjS0_ZfJ0']

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
            # set variables for subsections of the data
            snippet = item.get('snippet', {})
            stats = item.get('statistics', {})

            youtube_id = item.get('id', {})
            publishedAt = snippet.get('publishedAt', {})
            channelId = snippet.get('channelId', {})
            channelTitle = snippet.get('channelTitle', {})
            title = snippet.get('localized', {}).get('title', {})
            description = snippet.get('localized', {}).get('description', {})
            tags = snippet.get('tags', {})
            viewCount = stats.get('viewCount', {})
            likeCount = stats.get('likeCount', {})
            dislikeCount = stats.get('dislikeCount', {})
            favoriteCount = stats.get('favoriteCount', {})
            commentCount = stats.get('commentCount', {})
            topicCategories = item.get('topicDetails', {}).get('topicCategories', {})

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
    with open_csv_w('../output/youtube-video-information.csv') as csvfile:
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
