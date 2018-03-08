import json
import datetime
import csv
import time
import ssl
import requests
# from utils import request_until_succeed, open_csv_w
from secrets import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET
from utils import open_csv_w

context = ssl._create_unverified_context()
# access tokens
access_token = FACEBOOK_APP_ID + "|" + FACEBOOK_APP_SECRET

# handling different errors depending on the validity of the Facebook ID collected by humans
def custom_request(url):
    r = requests.get(url)
    success = False
    while success is False:
        try:
            # print(r.status_code)
            response = json.loads(r.text)
            if r.status_code == 200:
                success = True
                # this is for pooping out when there's an error
                if response.get('error'):
                    return None
            elif r.status_code == 404 or r.status_code == 400:
                return None
        # this is for continuing to try if there is rate
        except Exception as e:
            print(e)
            time.sleep(5)

            print("Error for URL %s: %s" % (url, datetime.datetime.now()))
            print("Retrying.")
    return r.text

# function to run IDs through API to see whether they are valid
def proof_facebook_ids(fb_id):

    # constructing the url for an http request for the Facebook API
    base ='https://graph.facebook.com/v2.9'
    page_id = "/%s/" % fb_id
    extra_parameters = '?access_token=%s' % access_token
    url = base + page_id + extra_parameters

    # variables for spreadsheet
    validity = ""
    processed_id = fb_id
    error_message = ""


    # retrieve data
    resp = custom_request(url)
    if resp:
        validity = True
        data = json.loads(custom_request(url))
        error_message = None
    else:
        validity = False
        r = requests.get(url)
        response = json.loads(r.text)
        error_message = response["error"]["message"]

    # prep data for csv
    id_data = [validity,
            processed_id,
            error_message]

	#write the csv
    with open_csv_w('../output/cleaned_ids.csv') as f:
    	writer = csv.writer(f)
    	writer.writerow(id_data)


# run the proofer
if __name__ == '__main__':
    # set array of IDs you want to proof
    fb_ids = []

    with open_csv_w('cleaned_ids.csv') as f:
    	writer = csv.writer(f)
    	writer.writerow(["id",
    			"valid",
    			"error"])
    # iterate through all the
    for fb_id in fb_ids:
        proof_facebook_ids(fb_id)
