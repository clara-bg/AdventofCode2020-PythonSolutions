# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 07:01:18 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 14
In an ideal world I would take out the identical bits oof the part A and B routine and put them in their own function but eh.
'''

from itertools import product

#This chunk here parses the input data
with open('14.txt', 'r') as file:
    data = file.read().splitlines()
    for i in range(len(data)):
        data[i] = data[i].replace(']', '').replace('[', ' = ').split(' = ') #Looks something like  ['mask', '01111X110010000X01001100X0000000001X'], ['mem', '28748', '8402'], ['mem', '9833', '7040']

# I seperated this from the other routines as both part A and part B use this
def addition(memory, base):
    sum = 0
    for i in memory:
        sum += int(memory[i], base)
    return sum

# Function for part A
def part_A(data):
    memory = {}
    mask = []
    for i in data:
        type = i[0]
        if type == 'mask':
            mask = list(i[1])
        elif type == 'mem':
            binary = list(bin(int(i[2]))[2:].zfill(36)) # This line does quite a lot. It changes the decimal mem value to binary. zfill adds 0s infront. Output looks like ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '1', '1', '0', '1', '0', '0']
            for j in range(len(mask)):
                if mask[j] != 'X':
                    binary[j] = mask[j] #This swaps the values of the mask that override the binary values
            memory[int(i[1])] = ''.join(binary) # Combines memory location with binary value in a dictionary eg. 9833: '011110110010000001001100100000000010'
    return addition(memory, 2) # Uses the addition function and returns the sum of all the binary values in decimal

# Function for part B
def part_B(data):
    memory = {}
    mask = []
    for i in data:
        type = i[0]
        if type == 'mask':
            mask = list(i[1])
        elif type == 'mem':
            binary = list(bin(int(i[1]))[2:].zfill(36))
            for x in range(len(mask)):
                if mask[x] != '0':
                    binary[x] = mask[x]
            binary = ''.join(binary)
            new_binary = binary.replace('X', '{}') 
            for j in product('01', repeat=binary.count('X')): # Cartesian product of 01 the number of times X is in binary example output => ('1', '0', '1', '0', '0')
                address = int(new_binary.format(*j),2) # *args for variable j length. This returns the decimal.
                memory[address] = i[2]
    return addition(memory, 10)

print('Part A: The sum of the values in memory:', part_A(data))
print('Part B: The sum of the values in memory:', part_B(data))
