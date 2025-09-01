These Snap tools are a set of simple web scrapers intended to get patch notes from the Marvel Snap website or card stats from snap.fan

SnapCard.py 
    
    grabs a card from snap.fan and provides the card cost, power, and ability. I occasionally use this as a quick-fetch to grab card data 
    for the weekly card discussions on /r/marvelsnapcomp.

SnapOTA-MainPage.py:
    
    uses the main marvel snap website and requests the page for the latest ota or patch notes, parses and outputs the 
    page to a text file for easy formatting into a reddit post. You will need to head to marvelsnap.com/news to get the page url.

SnapOTA.py:

    is similar to the main page except it requires the cloudfront URL and retrieves the full body and parses that for the notes, 
    same output as above. The cloudfront url is the one that you will get if you click on the OTA or Patch notes from within the game client.  
