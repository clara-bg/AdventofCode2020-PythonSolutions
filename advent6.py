# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 07:22:57 2020

@author: Clara
"""


with open('6.txt', 'r') as file:
    data = file.read().split('\n\n')
    
def part_A(data):
    newdata=[]
    count = 0
    totalcount = 0
    for i in data:
        newdata.append(i.replace('\n', ''))  
    for i in newdata:
        s=set(i)
        count = len(s)
        totalcount+=count
    return totalcount

def part_B(data):
    totalcountb = 0
    for i in data:
        newlist = []
        countb = 0
        newlist.append(i.split('\n'))
        for j in newlist:
                count = len(set.intersection(*[set(k) for k in j]))
                totalcountb +=count
    return totalcountb

print('Part A: The sum of the counts is: ', part_A(data))
print('Part B: The sum of the counts is: ', part_B(data))
