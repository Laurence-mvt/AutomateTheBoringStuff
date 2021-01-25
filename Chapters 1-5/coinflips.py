#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:01:48 2021

@author: laurencefinch
"""
# program to simulate how often 6 consecutive heads/tails appears in 100 number of coin flips

import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    for i in range(100):
        flip = random.randint(0,1)
        flips.append(flip)
    
    count = 1
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for index, flip in enumerate(flips[1:]):
        
        previousFlip = flips[index-1]
        currentFlip = flip
        # if previous flip and current are the same, add one to count of flips
        if previousFlip == currentFlip:
            count +=1
            # if counts are 6, then add streak and break to next experiment 
            if count == 6:
                numberOfStreaks += 1
                break
        else: # previous and current flip are not the same 
            count = 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))