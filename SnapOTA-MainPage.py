from bs4 import BeautifulSoup
import requests
import os

snap_url = input("What is the Snap OTA URL this week? ")
content = requests.get(snap_url)

# This script uses the main page from MarvelSnap and can be used for both patch notes and OTA notes.
# check success status of get request, 200 = OK any other status code is bad and asks for OTA URL again.
# https://marvelsnap.com/balance-updates-june-26-2025/ can be used for test-gets.

if content.status_code != 200:
    snap_url = input("What is the Snap OTA URL this week? ")
else: 
    print(f"Get Request Status code is: {content.status_code} OK.")

# you can force the encoding to whatever you need. For example to force utf-8 use content.encoding = 'utf-8' as we do below.
# using content.encoding = content.apparent_encoding the code will attempt to use the chardet library to guess the encoding and set accordingly.

content.encoding = 'utf-8'

# Need to tell Beautifulsoup to use the text of the content and to set the parser. We'll use lxml as it is faster than html.parser.
# We'll then get the patch notes, strip leading and trailing characters, double spaces, and replace certain characters in the ota_patch.
# finally we reinforce the encoding to avoid a TypeError when outputting to text.

soup = BeautifulSoup(content.text, 'lxml')

ota = soup.find( class_='c-article__content').text.replace(u"\u00A0", " ").replace(u"\u2019", "'").replace("  ", " ").encode('utf-8', 'ignore')

# creating the directory to save the OTA notes, if it doesn't exist.
otaNotesDir = ('D:/Weasel-Repo/marvel-snap-tools/posts/')
os.makedirs(otaNotesDir, exist_ok=True)

with open(otaNotesDir+('MainPageOTANotes.txt'), 'wb') as f:
    f.write(ota)
    print('File OTANotes.txt Saved')