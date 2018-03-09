import csv
import pandas as pd
import glob
import os
from bs4 import BeautifulSoup

# the name of your archive
foldername = "facebook-lamthuyvo"
# make
rows = []
# open every file
message_pages = glob.glob("../data/"+foldername+"/messages/*")
print("preparing to scrape messages you have exchanged with " + str(len(message_pages)) + " people")

for message_page in message_pages:
    # open messages page
    with open(message_page) as fp:
        soup = BeautifulSoup(fp, "html5lib")
        #isolate all the threads
        threads = soup.find_all("div", class_="thread")

        for thread in threads:
            participants = thread.find(text=True, recursive=False).encode('utf-8').strip()
            # isolate all message meta data, each message and all participants per thread
            messages = thread.find_all("div", class_="message")
            for message in messages:
                # get the message writer
                user = message.find("span", class_="user").get_text().encode('utf-8').strip()
                date = message.find("span", class_="meta").get_text().encode('utf-8').strip()
                content = message.findNext('p').get_text().encode('utf-8').strip()

                # define data dictionary for each user
                row = {"user": user,
                       "date": date,
                       "content": content,
                       "participants": participants}
                rows.append(row)

# make a new csv and export it
with open('../output/all_messages.csv', "w") as csvfile:
    fieldnames = ["user", "date", "content","participants"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in rows:
        writer.writerow(row)
