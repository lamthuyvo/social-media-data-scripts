import requests
import csv
import sys
import time


def request_until_succeed(url):
    while True:
        try:
            res = requests.get(url, timeout=10)
        except Exception as e:
            print("ERROR: {0}".format(e))
            print("Retrying in 5s.")
            time.sleep(5)
            continue

        if res.status_code == 200:
            return res.text
        else:
            print("STATUS CODE {0} @ {1}\n".format(
                res.status_code,
                url,
            ))
            print("Retrying in 5s.")
            time.sleep(5)

def open_csv_w(filename):
    """Open a csv file in proper mode depending on Python verion."""
    import io
    return(io.open(filename, mode='a',encoding="utf-8") if sys.version_info[0] == 2 else
           io.open(filename, mode='a+', newline='',encoding="utf-8"))
