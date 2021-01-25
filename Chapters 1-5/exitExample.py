#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:48:45 2021

@author: laurencefinch
"""
import sys

while True:
    print("type exit to exit")
    response = input()
    if response == 'exit':
        sys.exit()
    print(f'You typed {response}.')