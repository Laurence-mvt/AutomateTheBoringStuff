#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:43:51 2021

@author: laurencefinch
"""
import random

messages = ['It is certain', 
            'It is decidedly so',
            'Yes definitely', 
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
outcomes = []

for i in range(1000):
    outcome = messages[random.randint(0, len(messages) -1)]
    outcomes.append(outcome)

counts = []
for item in messages:
    
    counts.append({'message': item, 
                   'count': str(outcomes.count(item)) })
                  
for count in counts:
    print(f'{count["message"]}: {count["count"]}')
    
    
    



