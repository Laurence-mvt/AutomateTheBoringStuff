#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:41:53 2021

@author: laurencefinch
"""
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3*number + 1)
        return 3*number + 1
    
try:
    number = int(input("number: "))
except ValueError:
    print("you must enter an integer")

while number != 1:    
    number = collatz(number)