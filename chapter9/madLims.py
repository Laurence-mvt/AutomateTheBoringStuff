#! python3
# madLims.py - Allows users to add their own adjectives, nouns, adverbs and verbs to an Edward Lear limerick, which is saved to a new text file
# https://www.public-domain-poetry.com/edward-lear/more-nonsense-limerick-19-23256

import pyinputplus as pyip
from pathlib import Path
import re

# get user input for adjective, noun, verb, adjective
userName = pyip.inputStr('Enter your name:  ').title()
adj1 = pyip.inputStr('Enter an adjective:   ').lower()
noun = pyip.inputStr('Enter an noun:    ')
verb = pyip.inputStr('Enter an verb:    ').lower()
adj2 = pyip.inputStr('Enter an adjective:   ').lower()

# open new text file 
newPoem = open(f"{userName}'s Poem", 'w')

# load text from template text file
template =  """There was a ADJECTIVE1 person of Brill,
            Who purchased a NOUN with a frill;
            But they said, "Don't you wish,
            You mayn't VERB like a fish,
            You ADJECTIVE2 old person of Brill?"""

""" Original version: There was an old person of Brill, by Edward Lear
    There was an old person of Brill,
    Who purchased a shirt with a frill;
    But they said, "Don't you wish,
    You mayn't look like a fish,
    You obsequious old person of Brill?"       """

# sub words using regex
newVersion = template
inputRegex = re.compile(r'ADJECTIVE1')
newVersion = inputRegex.sub(adj1, newVersion)
inputRegex = re.compile(r'NOUN')
newVersion = inputRegex.sub(noun, newVersion)
inputRegex = re.compile(r'VERB')
newVersion = inputRegex.sub(verb, newVersion)
inputRegex = re.compile(r'ADJECTIVE2')
newVersion = inputRegex.sub(adj2, newVersion)

# write to new text file and print to screen
newPoem.write(newVersion)
newPoem.close()

print(f"{userName}'s Poem:".center(30))
print(f"{newVersion}")