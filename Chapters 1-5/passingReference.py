#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:29:17 2021

@author: laurencefinch
"""
def eggs(someParameter):
    someParameter.append('Hello')
    
spam = [1,2,3]
eggs(spam)
print(spam)

def eggs(someParameter):
    someParameter = someParameter * 2

bacon = 3
eggs(bacon)
print(bacon)