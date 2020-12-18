# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:34:59 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 18
Regex at the start is probably overkill, you could loop through to remove spaces as opposed to keep not spaces.
In an ideal world the two funcitons would be combined as they are largely similar.
'''
import re

file = open('18.txt').read()
input = file.splitlines()

input = [re.findall('\(|\d+|\*|\+|\)',x) for x in input] # The regex here basically removes the white spaces from the expressions, saving each expression as a list in the list input

def part_A(expressions):
    value = None
    operator = None
    level = 0 # Level is basically a way to keep track of the bracket we're in
    stack = [] # Sort of keeps track of the number of brackets 
    for i in expressions:
        if i == '(':
            level = level + 1
            stack.append(i)
        if i == ')':
            level = level - 1
            stack.append(i)
            if level == 0:
                i = part_A(stack[1:-1]) # This is quite exciting - it recursively solves each bracket until we're back at level 0, the splicing removes the brackets
                stack = []
        if i not in '()':
            if level > 0: # For brackets at the start
                stack.append(i)
            else:
                if i in '*+':   # Next bit does the actual operations
                    operator = i
                else:
                    i = int(i)
                    if value == None:
                        value = i
                    else:
                        if operator == '*':
                            value = value * i
                        else:
                            value = value + i
    return str(value)

def part_B(expressions): # This routine is very similar, note that values is a list rather than an int 
    values = None
    operator = None
    level = 0
    stack = []
    for i in expressions:
        if i == '(':
            level = level + 1
            stack.append(i)
        if i == ')':
            level = level - 1
            stack.append(i)
            if level == 0:
                i = part_B(stack[1:-1])
                stack = []
        if i not in '()':
            if level > 0:
                stack.append(i)
            else:
                if i in '*+':
                    operator = i
                else:
                    i = int(i)
                    if values == None:
                        values = [i]    # Initialises values with the first found integer
                    else:
                        if operator == '*':
                            values.append(i) # Values to be multiplied go here
                        else:
                            values[-1] = values[-1] + i # if operator = '+'
    total = 1            # multiplication happens here because addition takes precedence
    for v in values:
        total = total * v
    return str(total)

result = [int(part_A(x)) for x in input] # result is the list of the evaluation of each expression(line)
print('Part A: The sum of the resulting values:', sum(result))
result = [int(part_B(x)) for x in input]
print('Part B: The sum of the resulting values:',sum(result))








