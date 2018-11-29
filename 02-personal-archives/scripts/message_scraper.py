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
message_pages = glob.glob("../data/"+foldername+"/messages/inbox/*")
print("preparing to scrape messages you have exchanged with " + str(len(message_pages)) + " people")

def get_text(el, *args, **kwargs):
    found_el = el.find(*args, **kwargs)
    if found_el is None:
        return None
    else:
        return found_el.get_text().strip()

for message_page in message_pages:
    # open messages page
    with open(message_page+"/message.html") as fp:
        soup = BeautifulSoup(fp, "html5lib")
        chat_name = message_page.replace("../data/"+foldername+"/messages/inbox/","")
        #isolate all the threads
        threads = soup.find_all("div", class_="uiBoxWhite")
        participants = get_text(soup, "div", class_="_2lel")
        for thread in threads:

            # get the message writer
            user = get_text(thread,"div", class_="_2lel")
            date = get_text(thread,"div", class_="_2lem")
            content = get_text(thread,"div", class_="_2let")
            # define data dictionary for each user
            row = {"user": user,
                   "date": date,
                   "content": content,
                   "participants": participants,
                   "chat_name": chat_name}
            rows.append(row)



# make a new csv and export it
with open('../output/all_messages.csv', "w") as csvfile:
    fieldnames = ["user", "date", "content","participants", "chat_name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in rows:
        writer.writerow(row)
