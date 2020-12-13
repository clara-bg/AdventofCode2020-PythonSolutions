# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 08:06:56 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 13
Today was a big step up essentially you had to use various principles of modular arithmetic to predit when the next bus is after aa specified time.
Part B uses Chinese Factor Theorem.
For the second part of part B I used an algorithm I found online to find the x mod y statements for CFT
Seeing as I don't understand CFT I didn't include it in the code but you can feed the output into an online decoder.
'''

# This chunk just parses the data
data = open('13.txt').read().split('\n')
timestamp = int(data[0])
bus_ids=[]
for i in data[1].split(','):
    if i != 'x':
        bus_ids.append(int(i)) # A list of the numbers in the inout excluding the timestamp
        
# This next routine is part A
minutes = 0
while True:
  success = 0
  for i in bus_ids:
    if (timestamp + minutes) % i == 0:
      success = i
  if success != 0:              # The condition to exit the loop is that the total time (timestamp + minutes waited) be divisible by one of the bus_ids times
    print('ID of earliest bus * minutes waiting for the bus:', success * minutes)
    break
  minutes += 1


# This next routine is part B
print('Values to feed into an online Chinese Factor Theorem solver:')
new_bus_ids = list(enumerate(bus_ids)) # What it looks like => [(0, 19), (1, 41), (2, 859), (3, 23), (4, 13), (5, 17), (6, 29), (7, 373), (8, 37)]
for j in new_bus_ids:
    index,value = j 
for value, index in new_bus_ids:        # algorithm for finding the CFT inputs
    value = -value
    while value < 0:
      value += index
    print(value, 'mod', index)
    
    
'''To get the answer to part be you need to take the x outputs and put them into an online cft solver - dcode is pretty good'''
