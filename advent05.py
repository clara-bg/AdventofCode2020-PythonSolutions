# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 07:03:51 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 5
Today's challenge was basically to write a kind of binary search algorithm to work out the row and seat of the codes provided on a plane.
Part A asked us to find the greatest seat ID (row*8+seat)
Part B asked us to find the missing seat ID
'''

with open('5.txt', 'r') as file:
    data = file.read().split('\n')

# The algorithm for the rows
def binary_row_search(data, low, high):
    for i in data:
        mean = low + (high - low) // 2
        if i == 'F':
            high = mean
        else:
            low = mean + 1
    return low

# The algorithm for the columns
def binary_column_search(data, low, high): 
    for i in data:
        mean = low + (high - low) // 2
        if i == 'L':
            high = mean
        else:
            low = mean + 1
    return low

#This calculates the seat ID for each code and appends it to a list called seat_ids
def get_seat_ids(data):
    seat_ids = []
    for i in data:
        row = binary_row_search(i[:7], 0, 127)
        column = binary_column_search(i[7:], 0, 7)
        seat_ids.append(row * 8 + column)
    return seat_ids

#This finds the maximum out of the seat IDs
def part_A(data):
    seat_ids = []
    seat_ids = get_seat_ids(data)
    maximum = max(set(seat_ids))
    return maximum

#This finds the missing seat ID in the list seat_ids    
def part_B(data):
    seat_ids = set(get_seat_ids(data))
    lowest = min(seat_ids)
    highest = max(seat_ids)
    for i in range(lowest,highest):
        if not i in seat_ids:
            return i 

print('Part A: The highest seat ID is: ', part_A(data))
print('Part B: Your seat ID is: ', part_B(data))
                
                
            
                
        
    
