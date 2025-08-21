from bs4 import BeautifulSoup
import requests
import os

card_name = input("Card Name? ")
card_name_stripped = card_name.replace(" ", "").strip().casefold()

agamotto_skill_cards = {
    "WindsofWatoomb": "Spell01Agamotto", 
    "TemporalManipulation": "Spell02Agamotto",
    "ImagesofIkonn": "Spell03Agamotto",
    "BoltsofBalthakk": "Spell04Agamotto"    
    }

if card_name_stripped in agamotto_skill_cards:
    card_name_stripped = agamotto_skill_cards[card_name_stripped]

fallen_one_fix = (
    "thefallenone", 
    "fallenone"
    )

if card_name_stripped in fallen_one_fix:
    card_name_stripped = "FallenOne"

url = ("https://snap.fan/cards/")
snapUrl = (url + card_name_stripped).strip()

content = requests.get(snapUrl)

if content.status_code != 200:
    card_name = input("Card Name? ").replace(" ", "-").strip().casefold()
    snapUrl = (url + card_name).strip()
else: 
    print(f"Get Request Status code is: {content.status_code} OK.")

content.encoding = 'utf-8'

# Need to tell Beautifulsoup to use the text of the content and to set the parser. We'll use lxml as it is faster than html.parser.
# We'll then get the patch notes, strip leading and trailing characters, double spaces, and replace certain characters in the ota_patch.
# finally we reinforce the encoding to avoid a TypeError when outputting to text.

soup = BeautifulSoup(content.text, 'lxml')

# Use CSS selector to find the card ability element using the full CSS path
ability_elem = soup.find(class_= "d-none d-lg-block")

if ability_elem:
    ability = ability_elem.get_text().replace("\n", " ").replace("Description", "").strip()
    ability_type = f"{ability}".encode('utf-8')
else:
    ability_type = b"Ability not found"

# Find the h3 with class "mt-3" that contains an unordered list with cost and power
card_stats = b"Stats not found"
h3_elem = soup.find("h3", class_="mt-3")
if h3_elem:
    ul_elem = h3_elem.find_next("ul")
    if ul_elem:
        cost = power = None
        for li in ul_elem.find_all("li"):
            text = li.get_text(strip=True)
            if text.startswith("Type: Spell"):
                type = text
                type = type.replace("Type: Spell", "Skill").strip()
            elif text.startswith("Type: Character"):
                type = text 
                type = type.replace("Type: Character", "Character").strip()
            if text.startswith("Cost:"):
                cost = text
            if text.startswith("Power:"):
                power = text
        if type == "Character":
            card_stats = f"{type} card with {cost} and {power}".encode('utf-8', 'ignore')
        else:
            card_stats = f"{type} card with {cost}".encode('utf-8', 'ignore')

# Create the directory if it doesn't exist

card_stats_dir = ('D:/Weasel-Repo/marvel-snap-tools/posts/')
os.makedirs(card_stats_dir, exist_ok=True)

# Write the card name, ability, and stats to a text file

with open(card_stats_dir + ('SnapCard.txt'), 'wb') as f:
    f.write(card_name.encode('utf-8', 'ignore') + b'\n' 
              + card_stats + b'\n'
              + ability_type + b'\n'
            )
    print(f'File SnapCard.txt Saved')