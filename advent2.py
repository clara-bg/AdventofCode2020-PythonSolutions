# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 07:35:10 2020

@author: Clara
"""

'''
Advent of Code 2020 day 2
This challenge was to do some password validation on a list of 1000 entries.
The most complicated part is to format the text file into something useful.
I split the text up in various ways to isolate the lower bound of the policy, the upper bound of the policy,
the letter delimited by these and finally the password itself into seperate lists.
This mass of code validates for both part a nad part b of the challenge and outputs the number of valid and invalid passwords for each.
'''


def aocday2():
#    19-39 is formatting the text input by splicing it into seperate lists
    f = open(r'C:\Users\Clara\Documents\adventofcode\2.txt', 'r')
    passwords = []
    keys = []
    value1 = []
    value2 = []
    letters = []
    validcount = 0
    invalidcount = 0
    lettercount = 0
    validcountb = 0
    invalidcountb = 0
    for line in f:
        key,value = line.split(': ')
        passwords.append(value[:len(value)-1])
        keys.append(key)
        val1, val2andletter = key.split('-')
        value1.append(int(val1))
        val2,letter = val2andletter.split(' ')
        value2.append(int(val2))
        letters.append(letter)
#        41-48 is the validation part of part A
    for j in range(len(passwords)):
        lettercount = passwords[j].count(letters[j])
        if (lettercount <= value2[j]) and (lettercount >= value1[j]):
            validcount+=1
        else:
            invalidcount += 1
    print('Part A: Number of valid passwords: ', validcount)
    print('Part A:Number of invalid passwords: ', invalidcount)
#   This last bit is the validation part for part B
    for j in range(len(passwords)):
        tracker = 0
        temp = passwords[j] 
        if temp[value1[j]-1] == letters[j]:
            tracker +=1
        if temp[value2[j]-1] == letters[j]:
            tracker +=1
        if tracker == 1:
            validcountb +=1
        else:
            invalidcountb+=1
    print('Part B: Number of valid passwords: ', validcountb)
    print('Part B:Number of invalid passwords: ', invalidcountb)
    
aocday2()