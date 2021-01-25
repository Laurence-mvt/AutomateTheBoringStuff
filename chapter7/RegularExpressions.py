import re

# automate the boring stuff, Chapter 6, RegEx practice question
# How would you write a regex that matches a number with commas for every three digits?

text = "match: 42, 1,234, 6,368,745 but not match: 12,34,567, or 1234"

# Step 1 - extract all numbers from text 
# regex to match all numbers:
numRegex = re.compile(r"""(
                        (\d)           # first number 
                        ([0-9,]*)       # any subsequent digits or commas
                        )""", re.VERBOSE)

mo = numRegex.findall(text)

# Step 2 - extract all complete numbers into a separate list (can include commas at end of string):
searchNumbers = []
for match in mo:
    searchNumbers.append(match[0])

# Step 3 - remove ending commas from numbers
""" # Here using list manipulation
for index, number in enumerate(searchNumbers):
    if number[-1] == ',':
        numBeChanged = list(number)             # convert number to list to allow deletion
        del numBeChanged[-1]                    # delete comma
        numBeChanged = ''.join(numBeChanged)    # recombine clean number as string
        searchNumbers[index] = numBeChanged     # add clean number to list of searchNumbers in place of unclean number
"""

# to do Step 3 using .sub() regex method:
endingComma = re.compile(r',$')
for index, number in enumerate(searchNumbers):
    searchNumbers[index] = endingComma.sub('', number)


# Step 4 - check each string against regex of format of a number with commas for every three digits
numRegex = re.compile(r'''(
                        (^(\d{1,3}))      # 1-3 of digits to start string
                        ((,\d{3})*$)      # subsequent sequences of ',ddd' including one that ends the string
                        )''', re.VERBOSE)

# check each string for correct format
cleanNumbers = []
for number in searchNumbers:
    mo = numRegex.search(number)
    if mo != None: # if number correctly formatted, add to list
       cleanNumbers.append(mo.group(0))
for num in cleanNumbers:
    print(num)