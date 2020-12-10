# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 07:47:17 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 7
Today's challenge was a big step up from the previous six days.
The hardest part about this was again formatting the data to be somewhat useful.
Not my finest code but it works.
Watch out for the recursive solution in part_B()
'''

with open('7.txt', 'r') as file:
    data = file.read().split('\n')


def part_A(data):
    dataset = {}
    for d in data:
        x = d[:-1].split(' contain ')
        colourtemp = x[0][:-5]
        for b in x[1].split(', '):
            if b != 'no other bags':
                colour = ' '.join(b.split(' ')[1:-1])
                if colour not in dataset:
                    dataset[colour] = set({})
                dataset[colour].add(colourtemp)
    
    colours = {'shiny gold'}
    added = True
    while added:
        added = False
        l = len(colours)
        for colour in colours:
            if colour in dataset:
                colours = colours | dataset[colour]
        if len(colours) > l:
            added = True
    return len(colours)-1

def part_B_setup(data):
    global dataset
    dataset = {}
    for d in data:
        x = d[:-1].split(' contain ')
        colourtemp = x[0][:-5]
        for b in x[1].split(', '):
            if b != 'no other bags':
                colour = ' '.join(b.split(' ')[1:-1])
                num = int(b.split(' ')[0])
                if colourtemp not in dataset:
                    dataset[colourtemp] = set({})
                dataset[colourtemp].add((colour, num))
            else:
                dataset[colourtemp] = set({})
    
# A recursive solution
def part_B(colour):
    total = 0
    for colourtemp, num in dataset[colour]:
        total += num * (1 + part_B(colourtemp))
    return total

print(part_A(data))
(part_B_setup(data))
print(part_B('shiny gold'))
