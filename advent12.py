# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 07:46:33 2020

@author: Clara
"""

'''
Advent of Code 2020 Day 12
Today was about following a list of cardinal directions and measuring displacement from the origin.
'''

with open("12.txt", "r") as file:
    data = file.read().splitlines()

#This handles the 'R' or 'L' inputs
def part_A_turning(direction_facing, direction, degree_turn):
    index = facing.index(direction_facing)
    if direction == 'L':
        direction_facing = facing[(index - degree_turn // 90) % 4] # You have to use mod 4 (length of turning) incase you get 0 as the index so it goes back to 3
    else:
        direction_facing = facing[(index + degree_turn // 90) % 4] # Mod to deal with values greater than 4 after teh addition
    return direction_facing
    
 
# This handles the cardinal inputs. Working position is a list with 2 elements which is why we're indexing 0 and 1
def movingfunc(direction, working_position, distance):
    if direction == 'N':
        working_position[1] += distance
        return working_position
    if direction == 'E':
        working_position[0] += distance
        return working_position
    if direction == 'S':
        working_position[1] -= distance
        return working_position
    if direction == 'W':
        working_position[0] -= distance
        return working_position
    
# This is the actual routine for part A and uses the previous 2 functions.
def part_A(data):
    working_position = [0,0]
    direction_facing = 'E'
    for i in data:
        direction = i[0]
        magnitude = int(i[1:])
        if direction in moving:
            if direction == 'F': # This needs a special case as it doesn't have a direction so you have to use direction_facing as an argument
                working_position = movingfunc(direction_facing, working_position, magnitude)
            else:
                working_position = movingfunc(direction, working_position, magnitude)
        elif direction in turning:
            direction_facing = part_A_turning(direction_facing, direction, magnitude)
    return (abs(working_position[0]) + (abs(working_position[1]))) # You have to use abs to convert it back to a scalar quantitity

# This deals with the 'R' and 'L' inputs for part 2. You might be able to combine this with the part_A turning function but I'm not sure how
def part_B_turning(waypoint_position, direction):  
    if direction == 'L':
        new_position = [-waypoint_position[1], waypoint_position[0]]
        return new_position
    elif direction == 'R':
        new_position = [waypoint_position[1], -waypoint_position[0]]
        return new_position

# This combines movingfunc and part_B_turning to return the Manhattan distance
def part_B(data):
    waypoint = [10, 1]
    working_position = [0, 0]
    for i in data:
        direction = i[0]
        magnitude = int(i[1:])
        if direction in turning:
            for i in range(magnitude//90):
                waypoint = part_B_turning(waypoint, direction)
        elif direction in moving:
            if direction == 'F':
                for i in range(magnitude):
                    working_position = [working_position[i] + waypoint[i] for i in range(len(working_position))]
            else:
                waypoint = movingfunc(direction, waypoint, magnitude)
    return (abs(working_position[0]) + (abs(working_position[1])))

moving= ['N', 'E', 'S', 'W', 'F']
facing = ['N', 'E', 'S', 'W']
turning = ['L', 'R']

print('The Manhattan distance between that location and the ship\'s starting position:', part_A(data))
print('The Manhattan distance between that location and the ship\'s starting position:', part_B(data))
            
