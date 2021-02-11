#! usr/bin/env bash
# parses multiple addresses depending on how many addresses they have

import re

testAddress1 = {'addresses': 'Addresses:\n'
               'work: [ Street address hidden ] New York NY 10017 United '
               'States\n'
               'Home: [ Street address hidden ] New York NY 10162 United '
               'States'}

testAddress2 = {'addresses': 'Addresses:\n'
               'work: [ Street address hidden ] New York NY 10017 United '
               'States'}

testAddress3 = {'addresses': 'Addresses:\n'
               'Home: [ Street address hidden ] New York NY 10162 United '
               'States'}
testAddress4 = {'addresses': 'Addresses:\n'
               'Seasonal: [ Street address hidden ] Glendale CA 91206 United '
               'States\n'
               'Home: 195 Stanton Street 6F New York NY 10002 United States'}
testAddress5 = {'addresses': 'Addresses:\n'
               'Work: 80 Broad Street Suite 1801 New York NY 10004 United '
               'States\n'
               'Home: [ Street address hidden ] New York NY 10022 United '
               'States'}
testAddress6 ={'addresses': 'Addresses:\n'
               'Work: [ Street address hidden ] New York NY 10017 United '
               'States'}
testAddress7 = {'addresses': 'Addresses:\n'
               'Seasonal: [ Street address hidden ] New York NY 10017 United '
               'States'}

addressBook = [testAddress1, testAddress2, testAddress3, testAddress4, testAddress5, testAddress6, testAddress7]

def countNewLines(addresses):
    newLineRegex = re.compile("\n")
    mo = newLineRegex.findall(addresses)
    return len(mo)

regexBoth = re.compile(r'((work: |Work: |Seasonal: )(.*)Home: (.*))', re.DOTALL)
regexWork = re.compile(r'((work: |Work: |Seasonal: )(.*))', re.DOTALL)
regexHome = re.compile(r'(Home: (.*))', re.DOTALL)

i = 1
for entry in addressBook:
    print(f'entry: {i}')
    numberLines = countNewLines(entry['addresses'])
    # if both work and home addresses
    if numberLines == 2: 
        moBoth = regexBoth.search(entry['addresses'])
        # would add address to entry here instead of printing
        for index, group in enumerate(moBoth.groups()):
            print(str(index) + str(group))
        # entry['homeAddress']
    # if only one address, check what type of address
    elif numberLines == 1:
        moHome = regexHome.search(entry['addresses'])
        moWork = regexWork.search(entry['addresses'])
        # check if work address
        if moWork != None:
            # would add address to entry here instead of printing
            print('work')
            for index, group in enumerate(moWork.groups()):
                print(str(index) +" "+ str(group))
        else:
            print('home')
            # would add address to entry here instead of printing
            for index, group in enumerate(moHome.groups()):
                print(str(index) +" " + str(group))
    # if no addresses
    else:
        # set both addresses to None
        continue
    i += 1


