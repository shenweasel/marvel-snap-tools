from bs4 import BeautifulSoup
import requests

snap_url = input("What is the Snap OTA URL this week? ")
content = requests.get(snap_url)

# check success status of get request, 200 = OK any other status code is bad and asks for OTA URL again.
# This uses the cloudfront page to get the update information, to navigate to that page you'll need to get the URL from the in-game announcement.
# https://d3hyqhf8hhr6vv.cloudfront.net/en/april-24th-balance-updates-ljiwue9232jw/ can be used for test-gets.

if content.status_code != 200:
    snap_url = input("What is the Snap OTA URL this week? ")
else: 
    print(f"Get Request Status code is: {content.status_code} OK.")

# you can force the encoding to whatever you need. For example to force utf-8 use content.encoding = 'utf-8' as we do below.
# using content.encoding = content.apparent_encoding the code will attempt to use the chardet library to guess the encoding and set accordingly.

content.encoding = 'utf-8'

# creating the soup, need to tell Beautifulsoup to use the text of the content and to set the parser. We'll use lxml as it is understood to be the fastest/most efficient. 
# then get the ota_date from a class search and the ota_patch notes will be from the body of the html.
# strip both of leading and trailing characters as well as replace certain characters in the ota_patch.
# finally we reinforce the encoding as without I was getting errors when attempting to output to file.

soup = BeautifulSoup(content.text, 'lxml')

ota_date = soup.find('h1', class_='sc-8d1736fe-5 bCQHOp').text.strip().encode('utf-8', 'ignore')

ota_patch = soup.body.text.replace(u"\u00A0", " ").replace(u"\u2019", "'").encode('utf-8', 'ignore')

# set full location for the output, location must exist prior to running as we're not creating the location within the script

ota_notes_dir = ('D:/Weasel-Repo/RandomProjects/MarvelSnapTools/posts/')

with open(ota_notes_dir+('OTANotes.txt'), 'wb') as f:
    f.write(ota_date + b"\n")
    f.write(ota_patch)
    print('File OTANotes.txt Saved')