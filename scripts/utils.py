import requests
import csv
import sys

def request_until_succeed(url):
    r = requests.get(url)
    success = False
    while success is False:
        try:
            if r.status_code == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)

            print("Error for URL %s: %s" % (url, datetime.datetime.now()))
            print("Retrying.")

    return r.text

def open_csv_w(filename):
    """Open a csv file in proper mode depending on Python verion."""
    return(open(filename, mode='a') if sys.version_info[0] == 2 else
           open(filename, mode='a+', newline=''))
