These Snap tools are a set of simple web scrapers intended to get patch notes from the Marvel Snap website or card stats from snap.fan

\Posts\

    The Posts directory is a directory for post templates that I use for common threads on reddit.com/r/marvelsnapcomp. Templates include
    Weekly discussions such as current card release predictions, weekly meta recap, weekly card release post-mortem, and Limited Time 
    Game Mode informational threads.

SnapCard.py 
    
    grabs a card from snap.fan and provides the card cost, power, and ability. I occasionally use this as a quick-fetch to 
    grab card data for the weekly card discussions on /r/marvelsnapcomp. 
    I've also created a discord bot that has this as a built in command for discord to fetch card info.  

SnapOTA.py

    Imports snapota_commands and based on cloudfront or main site fetches full Patch or OTA update notes, parses and outputs
    the page to a text file for easy formatting into a reddit post.

snapota_commands.py 

    Uses BeautifulSoup and Requests to scrape the main marvel snap website. It receives a web address from the SnapOTA.py app 
    and uses that to request the page for the latest ota or patch notes, parses and outputs the page to a text file for easy 
    formatting into a reddit post. You will need to head to marvelsnap.com/news to get the page url.

snapota_cloudfront.py:

    Original form of the snapota_commands, this used the cloudfront url to generate the same output. 
    This has been deprecated in favor of snapOTA.py/snapota_commands.py


SnapOTA-MainPage.py:
    Second evolution of the cloudfront.py this utilized the main page to get patch notes. 
    This has been deprecated in favor of snapOTA.py/snapota_commands.py

