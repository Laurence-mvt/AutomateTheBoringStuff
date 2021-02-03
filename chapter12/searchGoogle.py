#! usr/bin/env bash
# searchGoogle.py - Opens multiple search windows in Google

import bs4, requests, sys, webbrowser
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  -  %(message)s')
logging.disable(logging.CRITICAL)

print('Searching for results...')
# get search results
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# get results links
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('a')
searchResults = []
for linkElem in linkElems:
    
    logging.debug('linkElem(%s)', linkElem)

    if linkElem.get('href')[:13] == '/url?q=https:':    # if propper search result link, add to list of results
        searchResults.append(linkElem.get('href'))

# open first 5 results
numToOpen = min(5, len(searchResults))
for i in range(numToOpen):
    endOfUrl = searchResults[i].index('&')
    webbrowser.open(searchResults[i][7:endOfUrl])
    print(searchResults[i][7:endOfUrl])