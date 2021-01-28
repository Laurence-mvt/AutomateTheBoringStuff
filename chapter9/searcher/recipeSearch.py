#! python3
# searcher.py - searches recipe text files for users inputed ingredients and returns recipes with those ingredients 
# returns the file name and line ingredient is mentioned (for practice sake)
# Usage: python searcher.py <searchFor>

from pathlib import Path
import pyinputplus as pyip
import re
import os
import pprint

# set path as current directory
currentDir = Path.cwd()

# get all files in current directory as list
# create generator object to be able to search for txt file
textFiles = currentDir.glob('*.txt')    # get all text file paths
niceTextFiles = list(textFiles)         # as a list

# get user input
ingredients = pyip.inputStr('Enter ingredients, separated by a space, to search for a recipe:  ', blockRegexes=[r'[0-9]']).strip()

# separate ingredients as a list and initialize as regular expressions
ingredients = '|'.join(ingredients.split())  # separate user inputed ingredients and join them, separated by '|' for later regex

# create a regex for each ingredient
ingredientsRegex = re.compile(ingredients)

# keep track of matches for each file (recipe). One match = {'recipeName': filename, 'ingredients': 'a b c d', 'line1': 'lineText'}
matches = []

# iterate over each file
for recipeFile in niceTextFiles:

    # open file
    recFile = open(recipeFile, 'r')

    # get recipe name as string
    recipeName = Path(recipeFile).stem
    
    # create one match object
    match = {'recipe': recipeName,
            'ingredients': []} 
    matchedIngredients = []

    # search for user inputed regex (consider case insensitive and mispelled words)
    # loop over each line
    lineNum = 1
    for index, line in enumerate(recFile.readlines()):
        if index == 0: 
            match['recTitle'] = line     # recipe title on top line of text file
        # search for regex matches
        mo = ingredientsRegex.findall(line)

        # if matches found in line, add line and ingredients to match
        if len(mo) > 0:    
            match[f'line {lineNum}'] = line 
            for word in mo:
                match['ingredients'].append(word.title())
        
        lineNum += 1 
    # append match to matches
    matches.append(match)

    # close file 
    recFile.close()


# Identify which recipes are perfect/partial matches
# loop over matches

# get lines from each recipe
recLines = []
recLinesPerfect = []
recLinesPartial = []

"""for recipe in matches:
    recipeCopy = recipe.copy()
    recipeCopy.pop("recipe")
    recipeCopy.pop("ingredients")
    recipeCopy.pop("recTitle")
    recLines.append(recipeCopy)"""

perfect = []
partial = []
somePerfect = False
somePartial = False

for recipe in matches:
    if len(list(set(recipe["ingredients"]))) == len(ingredients.split('|')):
        # perfect match for all ingredients
        perfect.append(recipe)
        recipeCopy = recipe.copy()
        recipeCopy.pop("recipe")
        recipeCopy.pop("ingredients")
        recipeCopy.pop("recTitle")
        recLinesPerfect.append(recipeCopy)
        somePerfect = True
    elif len(list(set(recipe["ingredients"]))) > 0:
        # partial match
        partial.append(recipe)
        recipeCopy = recipe.copy()
        recipeCopy.pop("recipe")
        recipeCopy.pop("ingredients")
        recipeCopy.pop("recTitle")
        recLinesPartial.append(recipeCopy)
        somePartial = True


# print output to screen
print()

if somePerfect == True:
    # print out perfect matches
    print('PERFECT MATCHES'.center(40))
    for index, recipe in enumerate(perfect):
        print(f"File Name: {recipe['recipe']}".center(40))
        print('-'*40)
        print(f"Recipe:  {recipe['recTitle']}")
        print(f"Ingredients: {', '.join(list(set(recipe['ingredients'])))}")
        print()
        for k, v in recLinesPerfect[index].items():
            print(str(k) + ': ' + str(v))
        print()
        print()

if somePartial == True:
    # print partial matches
    print('PARTIAL MATHCES'.center(40))
    for index, recipe in enumerate(partial):
        print(f"File Name: {recipe['recipe']}".center(40))
        print('-'*40)
        print(f"Recipe:  {recipe['recTitle']}")
        print(f"Ingredients: {', '.join(list(set(recipe['ingredients'])))}")
        print()
        for k, v in recLinesPartial[index].items():
            print(str(k) + ': ' + str(v))
        print()
        print()
elif somePerfect == False:
    print('No matches for these ingredients :(')