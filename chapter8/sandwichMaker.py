#!python3
# SandwichMaker.py - A program to order a sandwich based on user input and calculate the price of the total sandwich, to practice input validation

import pyinputplus as pyip

# keep track of order to display at end:
order = {}

# bread type:
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered = True)
order["bread"] = bread

# protein:
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
order["protein"] = protein

# cheese:
wantCheese = pyip.inputYesNo('Want cheese?')
# type of cheese
cheese = ''
if wantCheese == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
order["cheese"] = cheese

# extras
wantExtras = pyip.inputYesNo('want any of the following? - mayo, mustard, lettuce, or tomato - (answer yes or no)' )
extras = {
    'mayo': 0,
    'mustard': 0,
    'lettuce': 0,
    'tomato': 0
}

if wantExtras == 'yes':
    print('ok, options coming at you fast then. answer yes or no')
    for k, v in extras.items():
        if pyip.inputYesNo(f'want {k}?') == 'yes':
            extras[k] = 1
else: 
    print('suit yourself')

# add extras to ordered
for k, v in extras.items():
    order[k] = v

# number of sandwiches
number = pyip.inputNum('How many sandwiches would you like?', min=1)
order['quantity'] = number


prices = {    
    'bread': {
        'wheat': 0.5,
        'white': 0.2,
        'sourdough': 0.7
    },
    'protein': {
        'chicken': 2,
        'turkey': 2,
        'ham': 1,
        'tofu': 1.5
    },
    'cheese': {
        'cheddar': 0.5,
        'Swiss': 0.6,
        'mozzarella': 0.7,
        'no': 0 # cost if they don't want cheese
    },
    'extras': {
        'mayo': 0.5,
        'mustard': .2,
        'lettuce': .3,
        'tomato': .5
    }
}

# calculate cost per sandwich
totalCost = 0
# cost of extras
extrasCost = 0
for k, v in extras.items():
    extrasCost += v * prices['extras'][k]

# bread
totalCost = prices['bread'][bread] + prices['protein'][protein] + prices['cheese'][cheese] + extrasCost

# cost for total order 
Cost = round(totalCost * number, 2)

def printPrettySandwich(itemsDict, leftWidth, rightWidth):
    print()
    print('Your order is:'.center(leftWidth + rightWidth))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


printPrettySandwich(order, 10, 10)
print('-'*20)
print(f'Your total bill is ${Cost}')


