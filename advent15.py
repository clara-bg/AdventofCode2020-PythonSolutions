# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 07:29:07 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 15
Even though the execution of the program is shockingly slow I'm still proud of this one - nice and compact code.
'''
import time

input = [11,18,0,20,1,7,16]

def routine(rounds, input):
    history = {}
    for i in range(len(input)):
        history[input[i]] = i + 1 # A dictionary of the numbers which have been said
    final = input[-1]
    for i in range(len(input) + 1, rounds + 1): # Add 1 so that final is 2020 not 2019
        if final in history:
            num = i - 1 - history[final] # difference between the turn number when it was last spoken and the turn number of the time it was most recently spoken before then
        else: # If the number hasn't been said before
            num = 0
        history[final] = i - 1 #Because all the values of i were defined as one more earlier
        final = num
    return final

start_time = time.time()
print('Part A: The 2020th number spoken:', routine(2020, input))
print('Part B: The 30000000th number:', routine(30000000, input))
print('Time taken for program execution:', time.time() - start_time)
