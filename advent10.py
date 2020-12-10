# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 08:26:58 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 10
Part A of this challenge was pretty straight forward especially using counter() instead of defining my own dictionary and making it clunky.
Part B is pretty interesting, it looks like an (O^n) problem so I used dynamic programing instead to make in polynomial.
'''

#for counter and default dict
import collections

#this formats the data and sorts it. Remember to add the final value which is three more than the greatest.
def init():
    with open('10.txt') as f:
        data = f.read().split()
    data = list(map(int, data))
    data.sort()
    data.append(max(data) + 3)
    return data

#This uses counter to build a dictionary where the key is the interval adn the value is the number of times it occurs in data.
def part_A(data):
    prev_value = 0
    nums = collections.Counter()
    for i in data:
        nums[i-prev_value] += 1
        prev_value = i
    return nums[1] * nums[3]

#This is a bit more tricky
#Use defaultdict here so that you don't start getting key errors everywhere
#In the for loop you're basically finding the combination of ways you can order three adjacent values of v and compounding that into combins
#We return combins on the largest item of data as it has the compounded calculations of all the previous values - basically has all the unique operations
def part_B(data):
    combins = collections.defaultdict(int)
    combins[0] = 1
    for v in data:
        combins[v] = combins[v - 1] + combins[v - 2] + combins[v - 3]
    return combins[max(data)]

init = init()
print("The number of 1-jolt differences multiplied by the number of 3-jolt differences: ", part_A(init))
print("The total number of distinct ways you can arrange the adapters to connect the charging outlet to your device: ", part_B(init))   
    