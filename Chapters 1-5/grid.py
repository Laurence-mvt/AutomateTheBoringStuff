#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:55:13 2021

@author: laurencefinch
"""
# Character Picture Grid problem
# Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” 
#   drawn with text characters. The (0, 0) origin is in the upper-left corner, 
#   the x-coordinates increase going right, and the y-coordinates increase going down.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# for each row
for row in range(len(grid[0])):
    # print all the current row ie grid[0][row], grid[1][row], grid[2][row],...
    for i in range(len(grid)):
        print(grid[i][row], end="")
    # print new line
    print()
    
    
