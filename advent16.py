# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:21:32 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 16
Sorry for the ugly solution but it works
'''

import re


pattern = '([a-z]+ ?[a-z]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)'

with open('16.txt') as f:
    data = f.read().split('\n')

details = []
ticket_info = []
for i in range(len(data)):
    if data[i] == 'your ticket:':
        for j in range(i-1):
            details.append(data[j])
        for k in range(i+1, len(data)):
            ticket_info.append(data[k])
ticket_info.remove('')
ticket_info.remove('nearby tickets:')
ticket_info.remove(ticket_info[1])

detail_type = []
min_value_1 = []
max_value_1 = []
min_value_2 = []
max_value_2 = []
for line in details:
    match = re.search(pattern,line)
    detail_type.append(match.group(1))
    min_value_1.append(int(match.group(2)))
    max_value_1.append(int(match.group(3)))
    min_value_2.append(int(match.group(4)))
    max_value_2.append(int(match.group(5)))

ticket_info = [i.split(',') for i in ticket_info]

valid_nums = []
for i in range(len(detail_type)):
    for j in range(min_value_1[i], max_value_1[i]):
        valid_nums.append(j)
    for k in range(min_value_2[i], max_value_2[i]):
        valid_nums.append(k)
        
valid_nums = set(valid_nums)
invalid = 0
invalids = []
for line in ticket_info:
    for i in line:
      if not int(i) in valid_nums:
          invalid += int(i)
          invalids.append(line)
          
print('Part A:', invalid)


for i in invalids:
    for j in ticket_info:
        if i == j:
            ticket_info.remove(j)


ordered_fields = {}
for i in range(len(detail_type)-1):
    count = 0
    for line in ticket_info:
        for j in range(len(detail_type)-1):
            if (((int(line[i]) >= min_value_1[j]) and(int(line[i])<=max_value_1[j])) or ((int(line[i]) >= min_value_2[j]) and (int(line[i])<=max_value_2[j]))):
                count += 1
                break
    if count == len(detail_type):
        ordered_fields[detail_type[j]] = i
        
answer = 1
my_ticket = ticket_info[0]
departure_values = []
pattern2 = '(departure [a-z]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)'
for line in detail_type:
    match = re.search(pattern2,line)
    departure_values.append(int(match.group(1)))
for i in ordered_fields.keys():
    if i in set(departure_values):
        answer *= ordered_fields[i]
    
print('Part_B:',answer)
    














