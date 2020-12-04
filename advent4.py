# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:38:09 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 4
The challenge today was to validate passport entries according to certain criteria. 
In part A it asked us to ensure all necessary inputs for each passport were present: {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
In part B it asked us to validate each of those input according to limits we were given.
'''

with open('4.txt', 'r') as file:
    data = file.read().split('\n')

# This function formats the data into a list of dictionaries. 
def dataformat(data):
    separatedata = []
    passports = {}
    for line in data:
        if not line:
            separatedata.append(passports)
            passports = {}
        else:
            for element in line.split(' '):
                key, value = element.split(':')
                passports[key] = value
    if passports: separatedata.append(passports)
    return separatedata

# This function uses .issubset() to determine whether all the required elements are in the passport entry
def partA(separatedata):
    validcounter = 0
    validfields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    
    for element in separatedata:
        if validfields.issubset(set(element.keys())):
            validcounter +=1
            
    return validcounter

#The following functions are for part B and check each individual criteria against the limitations detailed in the challenge
def dyrcheck(element):
    if {'byr'}.issubset(set(element.keys())):
            byr = int(element['byr'])
            if (byr >= 1920) and (byr <= 2002):
                return True
            
def iyrcheck(element):
    if {'iyr'}.issubset(set(element.keys())):
            iyr = int(element['iyr'])
            if (iyr >= 2010) and (iyr <= 2020):
                return True
            
def eyrcheck(element):
    if {'eyr'}.issubset(set(element.keys())):
            eyr = int(element['eyr'])
            if (eyr >= 2020) and (eyr <= 2030):
                return True
            
def hgtcheck(element):
    if {'hgt'}.issubset(set(element.keys())):
            hgt = element['hgt']
            if (hgt[-2:] == 'cm') and (int(hgt[:-2]) >= 150) and (int(hgt[:-2]) <= 193):
                return True
            if (hgt[-2:] == 'in') and (int(hgt[:-2]) >= 59) and (int(hgt[:-2]) <= 76):
                return True
            
def hclcheck(element):
    if {'hcl'}.issubset(set(element.keys())):
            hcl = element['hcl']
            if (len(hcl) == 7) and (hcl[0] == '#') and (all(x in 'abcdef1234567890' for x in hcl[1:])):
                return True
            
def eclcheck(element):
    if {'ecl'}.issubset(set(element.keys())):
                ecl = element['ecl']
                if (ecl in  {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}):
                    return True

def pidcheck(element):
    if {'pid'}.issubset(set(element.keys())):
            pid = element['pid']
            if (len(pid) == 9) and (pid.isdecimal()):
                return True

# This function brings all the other part b functions together and checks whether each element (passport entry) is valid or not
def partB(separatedata):
    validpartb = 0
    for element in separatedata:
        if dyrcheck(element) and iyrcheck(element) and eyrcheck(element) and hgtcheck(element) and hclcheck(element) and eclcheck(element) and pidcheck(element):
            validpartb +=1
            
    return validpartb

formatted_data = dataformat(data)
print('Part A: Number of valid passports: ', partA(formatted_data))
print('Part B: Number of valid passports: ', partB(formatted_data))
