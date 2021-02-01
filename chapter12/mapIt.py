#! python3
# mapIt.py - opens Google maps in browser to location copied to clipboard, or entered in command line

import pyperclip, sys, webbrowser

location = ""

# read command line arguments
# if location entered, then location to look for is that location
if len(sys.argv) > 1:
    location = ' '.join(sys.argv[1:])

# else, read the clipboard contents
else:
    location = pyperclip.paste()


# open the web browser at google maps
webbrowser.open('https://www.google.com/maps/place/' + location)

