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
def get_page_info(fb_id):
    print(fb_id)

    # constructing the url for an http request for the Facebook API
    base ='https://graph.facebook.com/v2.9'
    page_id = "/%s/" % fb_id
    extra_parameters = '?access_token=%s' % access_token
    fields= '&fields=name,about,fan_count,talking_about_count,website,start_info'
    url = base + page_id + extra_parameters + fields

    # variables for spreadsheet
    error_message = ""

    # retrieve data and handle errors if ID is wrong
    resp = custom_request(url)
    if resp:
        data = json.loads(custom_request(url))
    else:
        r = requests.get(url)
        response = json.loads(r.text)
        error_message = response["error"]["message"]
        print error_message

    page_data_json = json.loads(custom_request(url))

    # set values if they exist for that page
    group_name = page_data_json.get('name')
    about = page_data_json.get('about')
    fan_count = page_data_json.get('fan_count')
    talking_about_count = page_data_json.get('talking_about_count')
    website = page_data_json.get('website')
    page_id = page_data_json.get('id')
    date_obj = page_data_json['start_info'].get('date')


    if date_obj:
        year = date_obj.get('year')
        month = date_obj.get('month')
        day = date_obj.get('day')
    else:
        year = None
        month = None
        day = None

    # prep data for csv
    # make a dictionary for each row
    page_data = {
        'group_name': group_name.encode('utf-8') if group_name else None,
        'about': about.encode('utf-8') if about else None,
        'fan_count': fan_count,
        'talking_about_count': talking_about_count,
        'website': website,
        'page_id': page_id,
        'year': year,
        'month': month,
        'day': day
    }

    return page_data


# run the proofer
if __name__ == '__main__':
    # set array of IDs for Facebook Pages for which you want to collect data
    fb_ids = [
    '36872601914',
    '390478684333910']

    with open('../output/pages_info.csv', 'w+') as f:

        fieldnames = ["group_name",
                        "about",
                        "fan_count",
                        "talking_about_count",
                        "website",
                        "page_id",
                        "year",
                        "month",
                        "day"]
    	writer = csv.DictWriter(f, fieldnames = fieldnames)

        writer.writeheader()

        # iterate through all the
        for fb_id in fb_ids:
            row = get_page_info(fb_id)

            writer.writerow(row)
