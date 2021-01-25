#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:14:37 2021

@author: laurencefinch
"""
spam = {'color': 'red',
        'age': 42}

for k, v in spam.items():
    print('Key: ' + k + 'Value: ' + str(v))
    
# the get(() method:
print(spam.get('color', 'white')) # returns color value if color exists as a key in spam, and 'white' if not

# the setdefault() method:
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)    

# can use "pretty print" pprint module's pprint() and pformat() functions to neatly print a dictionary's values
import pprint
pprint.pprint(count)

# If you want to obtain the prettified text as a string value instead of 
#   displaying it on the screen, call pprint.pformat() instead. 
string_output = pprint.pformat(count["d"])
print(f'string_output: {string_output}')

