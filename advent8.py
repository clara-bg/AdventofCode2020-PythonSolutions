# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:09:51 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 8
Sorry about the bruteforce approach in part B I couldn't think of anything better.
'''
with open('8.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

def routine(data):
    accumulator = 0
    i = 0
    seen_items = set([])
    while i < len(data):
        # I save every step I take into seen_items to establish when it loops for the second time and to define an exit condition,avoiding infinite loops.
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
    #This is only really relevant for part B of the challenge but it was easier to put it in routine()
    return accumulator, None

def part_B(data):
    for i in range(len(data)):
        newdata = data.copy()
        end = 0
        #only one of these next two statements will be successful so only one result will get returned. Every other trial will end in none and therefore break.
        if 'nop' in data[i]:    
            newdata[i] = data[i].replace('nop', 'jmp')
            result, end = routine(newdata)
        elif 'jmp' in data[i]:
            newdata[i] = data[i].replace('jmp', 'nop')
            result, end = routine(newdata)
        if end is None:
            break
    # a result is returned after every possible option is tried. There's definitely some kind of repeat until solution here but this works too, albeit inefficiently.
    return result

print('The value of the accumulator is: ', routine(data)[0]) #You have to specify index 0 as the function returns both the accumulator and its i value. This way it only outputs the accumulator.
print('The value of the accumulator is: ', part_B(data))
