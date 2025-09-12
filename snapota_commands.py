from bs4 import BeautifulSoup
import os
import requests
from datetime import date

def main():
    pass

def getOtaCloudfront(snap_url):

    content = requests.get(snap_url)
    content.encoding = 'utf-8'

    soup = BeautifulSoup(content.text, 'lxml')

    ota_date = soup.find('h1', class_='sc-8d1736fe-5 bCQHOp').text.strip().encode('utf-8', 'ignore')

    ota_patch = soup.body.text.replace(u"\u00A0", " ").replace(u"\u2019", "'").encode('utf-8', 'ignore')

    ota_notes_dir = ('D:/Weasel-Repo/marvel-snap-tools/posts/')

    with open(ota_notes_dir+('OTANotes.txt'), 'wb') as f:
        f.write(ota_date + b"\n")
        f.write(ota_patch)
        print('File OTANotes.txt Saved')

def getOtaMain(snap_url):

    content = requests.get(snap_url)
    content.encoding = 'utf-8'

    soup = BeautifulSoup(content.text, 'lxml')

    ota = soup.find( class_='c-article__content').text.replace(u"\u00A0", " ").replace(u"\u2019", "'").replace("  ", " ").encode('utf-8', 'ignore')

    otaNotesDir = ('D:/Weasel-Repo/marvel-snap-tools/posts/')
    os.makedirs(otaNotesDir, exist_ok=True)

    with open(otaNotesDir+(f'{date.today()}_MainPageOTANotes.txt'), 'wb') as f:
        f.write(ota)
        print('File OTANotes.txt Saved')

if __name__ == "__main__":
    getOtaCloudfront()
    getOtaMain()