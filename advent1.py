# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:43:20 2020

@author: Clara
"""
import string

'''
Advent of Code Challenge 1:
Part A:Code which finds the two items in the list provided which add to 2020 and multiply them.
Part B:Code which finds the three items in the list provided which add to 2020 and multiply them.
'''

'''
The function getlist reads all the values from the text file which i called 1.txt. 
For some reason it didnt like my file path but stackoverflow said to add an r before it and this worked (no clue why)
It then converts these into a list called f_list.
When reading from a file it appends \n to each value because theres a newline in the file.
To remove this I used the strip function and appended the new values to nextlist.
For the set function I turned nextlist into a set.
'''
def getlist():
    f = open(r'C:\Users\Clara\Documents\adventofcode\1.txt', 'r')
    f_list = list(f)
    global theset 
    global nextlist
    nextlist = []
    for i in f_list:
        nextlist.append(int(i.strip()))
    theset = set((nextlist))

'''
Part A:
This iterates through the list with two different variables, tests whether they add to 2020.
It multiplies them and prints the result.
'''
def twomultiples():
    for i in range(len(nextlist)-1):
        for j in range(len(nextlist)-1):
            if nextlist[i] + nextlist[j] == 2020:
                print(nextlist[i]*nextlist[j])
                return True

'''
Part B:
This iterates through the list with three different variables, tests whether they add to 2020.
It multiplies them and prints the result.
'''            
def threemultiples():
    for i in range(len(nextlist)-1):
        for j in range(len(nextlist)-1):
            for k in range(len(nextlist)-1):
              if nextlist[i] + nextlist[j] + nextlist[k] == 2020:
                   print(nextlist[i]*nextlist[j]*nextlist[k])
                   return True

'''
Part A but better:
It uses a set instead of a list.
This solution uses O(n) whereas twomultiples() is O(n**2) and threemultiples() is O(n**3)
It is more effecient.
'''    
def setfunc():
    othervalue = 0
    for i in theset:
        othervalue = 2020-i
        if othervalue in theset:
            print(i*othervalue)
            return True
    
              
          
getlist()                
twomultiples()
threemultiples()
setfunc()
