# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 07:38:08 2020

@author: Clara
"""
'''
Advent of Code 2020 Day 9
'''
import itertools

with open('9.txt') as f:
    data = f.read().split()

data = list(map(int, data))

def part_A(data):
    sums = []
    for i in range(25, len(data)):
        p = itertools.permutations(data[i-25:i], 2)
        for j in p:
            sums.append(sum(j))
        if data[i] not in sums:
            answer_A = data[i]
            return answer_A
            
def part_B(data,answer_A):
    start = 0
    end = 1  
    while True:
        s = sum(data[start:end])
        if s > answer_A:
            start += 1
            end = start + 1
            continue
        if s == answer_A:
            set_ = data[start:end]
            answer_B = sum([min(set_), max(set_)])
            return answer_B
        if data[start] > answer_A:
            break    
        end += 1

part_A = part_A(data)
print('The first number that cannot be expressed as the sum of two numbers within the last 25 is: ', part_A)
print('the encryption weakness in the XMAS-encrypted list of numbers:', part_B(data,part_A))
