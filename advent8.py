# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:09:51 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 7
'''
with open('8.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

def routine(data):
    accumulator = 0
    i = 0
    seen_items = set([])
    while i < len(data):
        if i in seen_items:
            return accumulator, i
        seen_items.add(i)
        instruction, value = data[i].split()
        if instruction == 'acc':
            accumulator += int(value)
        elif instruction == 'jmp':
            i += int(value)
            continue
        i += 1
    return accumulator, None

def part_B(data):
    for i in range(len(data)):
        newdata = data.copy()
        end = 0
        if 'nop' in data[i]:
            newdata[i] = data[i].replace('nop', 'jmp')
            result, end = routine(newdata)
        elif 'jmp' in data[i]:
            newdata[i] = data[i].replace('jmp', 'nop')
            result, end = routine(newdata)
        if end is None:
            break
    return result

print('The value of the accumulator is: ', routine(data)[0])
print('The value of the accumulator is: ', part_B(data))