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

addressBook = [testAddress1, testAddress2, testAddress3]

def countNewLines(addresses):
    newLineRegex = re.compile("\n")
    mo = newLineRegex.findall(addresses)
    return len(mo)

regexBoth = re.compile(r'(work: (.*)Home: (.*))', re.DOTALL)
regexWork = re.compile(r'(work: (.*))', re.DOTALL)
regexHome = re.compile(r'(Home: (.*))', re.DOTALL)


for entry in addressBook:
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



