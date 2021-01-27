#! python3
# madLibs.py - Allows users to add their own adjectives, nouns, adverbs and verbs to an Edward Lear limerick, which is saved to a new text file
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
template = Path('/Users/laurencefinch/Desktop/AutomateBoringStuff/AutomateTheBoringStuff/chapter9/templatePoem.txt').read_text()
print(f'template:   {template}')
print()
print()

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