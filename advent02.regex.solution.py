# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:59:30 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 2
I have two solutions for this on github this one uses regex as opposed to lots of string splicing and is MUCH cleaner.
Sadly it's not structured in functions but it didn't really make sense in this challenge as part B needs all the code from part A plus a few lines.
'''


import re

with open('2.txt', 'r') as file:
    data = file.read().split('\n')

pattern = '([0-9]+)-([0-9]+) ([a-z]+): ([a-z]+)'
valid_num_A = 0
valid_num_B = 0
for line in data:
    count = 0
    match = re.search(pattern, line)
    min_value = int(match.group(1))
    max_value = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)
    count = password.count(letter)
    if count >= min_value and count <= max_value:
        valid_num_A += 1

# Part B

    if password[min_value -1] == letter and not password[max_value -1] == letter:
        valid_num_B += 1
    if password[max_value -1] == letter and not password[min_value -1] == letter:
        valid_num_B += 1

        
print('Part A: There are', valid_num_A, 'valid passwords')
print('Part B: There are', valid_num_B, 'valid passwords')