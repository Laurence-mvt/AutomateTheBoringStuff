# notes on web scraping from chapter 12

# to open webpages
import webbrowser 
webbrowser.open('https://<url>')

# download webpages
import requests

res = requests.get('url')   # returns a response object

res.status_code # always check response object status code to check that the request was successful
res.raise_for_status() # raises exception if error occurred in request
downloadFile = open('filename.extension', 'wb') # wb for write binary mode, write binary data to preserve Unicode encoding of the text

for chunk in res.iter_content(100000):  #a chunk of bytes, 100000 generally a good size
    downloadFile.write(chunk)

downloadFile.close()

# when inspecting elements using browser's developer tools, can right click on element, and copy selector
# use Beautiful Soup 4 module (bs4) to parse downloaded html files

# create beautiful soup object that can be parsed, to access specific parts of the webpage
import requests, bs4
res = requests.get('url')   # download webpage
res.raise_for_status()      # check for errors
exampleSoup = bs4.BeautifulSoup(res.text, 'html.parser')     # passes the text attribute of response object to bs4 to be parsed
#   can use 'lxml.parser' for faster parsing (must be installed)

# use bs4's select() method to select element by css selector
# returns a list like object of tag objects, one tag for every match
elems = exampleSoup.select('#author')
type(elems) # <class 'bs4.element.ResultSet'>
len(elems) # 1
str(elems[0]) # '<span id="author">Al Sweigart</span>'
elems[0].getText() # Al Sweigart    i.e. gets inner html of tag
elems[0].attrs # gets attributes as a dictionary, e.g. here = {'id': 'author'}

elems[0].get('id') # 'author', i.e. returns value of attribute with key = 'id'



