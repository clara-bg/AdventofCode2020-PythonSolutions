# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:38:35 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 3:
Today's challenge was to use the map of #s and .sand determine, using different paths to travel across it, how many #s (or trees) you encounter.
The first section of the program reads in the data from file and splits it such that each row of data is saved into an element in the list datalist.
The second second section is the function countingtrees() this takes the list and then the horixontal step count and vertical stepcount.
The length and width denote the dimensions of the map.
I had to divide length by y as when y is greater than one, the total vertical points you touch on your way down decreases. Not reducing length result in too many values of i.
I did the modulus function on the x*i as otherwise the values would overflow the boundaries of width.
I then validated whether the value in the 2D array was a # (tree)
Part two is just subbing in different values for the x and y parameters and multiplying the result of the number of trees on each path.
'''

# read the data into the program and format into an array.

f = open(r'C:\Users\Clara\Documents\adventofcode\3.txt', 'r')
datalist = []
for line in f:
    datalist.append(list(line.strip('\n')))

# Solution to Part A:

def countingtrees(datalist, x, y):
    treecount = 0
    length, width = len(datalist), len(datalist[0])
    for i in range(length // y):
        row = i*y
        column = (x*i) % width
        if datalist[row][column] == '#':
            treecount +=1
    return treecount
    
    
print('Part A: number of trees encountered: ', countingtrees(datalist, 3,1))

# Solution to Part B:

slope1 = countingtrees(datalist, 1,1)
slope2 = countingtrees(datalist, 3,1)
slope3 = countingtrees(datalist, 5,1)
slope4 = countingtrees(datalist, 7,1)
slope5 = countingtrees(datalist, 1,2)

print('Part B: number of trees encounteres: ', slope1*slope2*slope3*slope4*slope5)
