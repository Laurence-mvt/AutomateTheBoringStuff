#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:45:52 2021

@author: laurencefinch
"""

while True:
    age = input('age:')
    if age.isdecimal():
        break
    print('must give number')
    
spam = 'hi laurence 23'

print(spam.startswith('h'))

print(spam.startswith('12'))
print(spam.endswith(' 23'))