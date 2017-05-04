import requests
import csv
import sys
import time


def request_until_succeed(url):
    while True:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        else:
            time.sleep(5)
            print("ERR: {0} @ {1}\n".format(
                res.status_code,
                url,
            ))
            print("Retrying.")

    # return r.text

def open_csv_w(filename):
    """Open a csv file in proper mode depending on Python verion."""
    return(open(filename, mode='a') if sys.version_info[0] == 2 else
           open(filename, mode='a+', newline=''))
