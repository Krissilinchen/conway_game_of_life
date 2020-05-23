# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:49:35 2020

@author: Kristin Geßler
"""

#Exercise 12.2 (30 Points)
#Task: The “Conway’s game of life” is a two-dimensional generalization of the cellular automata
#described in this chapter, and it is also equivalent to a universal Turing Machine [26, 27].
#Implement the evolution rule on a twodimensional grid of size 300×300
#with periodic boundary conditions using numpy.
#Try to follow the evolution of a random initial state for 200 steps.

#Rules: 
#1. Any dead cell with exactly 3 live neighbors becomes alive, by reproduction.
#2. Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation.
#3. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right.
#4. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation.

#Generally:
#Each cell has 8 neighbours
    
import numpy as np
from PIL import Image


# 0 = False, 1 = True
# index is number of neighbours alive; here we consider the rule from the sight of the ALIVE cells
rule_alive = np.zeros(8+1, np.uint8)  # default: all to dead; datatype = unsigned integer (0 to 255)
rule_alive[[2,3]] = 1 # alive stays alive <=> 2 or 3 neighbours
#print(rule_alive)

# index is number of neighbors alive; here we consider the rule from the sight of the DEAD cells
rule_dead = np.zeros(8+1, np.uint8)   # default: all to dead; datatype = unsigned integer (0 to 255)
rule_dead[3] = 1 # dead switches to living <=> 3 neighbors
#print(rule_dead)

iterations = 200
dimension = 300
images = []

#state is randomly initialized: 300x300 matrix
state = np.random.choice([0, 1], size=dimension*dimension)
state = np.reshape(state,(dimension, dimension))
#print(state)

for k in range(iterations):
    number_of_neighbours = np.roll(state,1, axis = 0)\
                        + np.roll(state,-1, axis = 0)\
                        + np.roll(state,1, axis = 1)\
                        + np.roll(state,-1, axis = 1)\
                        + np.roll(state, [1, 1], axis=(0, 1))\
                        + np.roll(state, [-1, 1], axis=(0, 1))\
                        + np.roll(state, [1, -1], axis=(0, 1))\
                        + np.roll(state, [-1, -1], axis=(0, 1))
    # use \ to divide the calculation                    
    #print(number_of_neighbours)
    for i in range(dimension):
        for j in range(dimension):
            if state[i][j] == 1:
                state[i][j] = rule_alive[number_of_neighbours[i][j]]
            else:
                state[i][j] = rule_dead[number_of_neighbours[i][j]]
    #print(state)

    im = Image.fromarray(255*state)# 1 becomes 255 (due to pixel)
    images.append(im)
    
images[0].save(fp='animated_game_of_life.gif', format='GIF', append_images=images[1:],
         save_all=True, duration=200, loop=0)    

                     
 

###############################################################################
# #Testing:
# state_test = np.arange(0,16).reshape(4,4)
# print(state_test)
# print()
# print()

# img_roll_down = np.roll(state_test, 1, axis = 0) # rolls y downwards 
# img_roll_up = np.roll(state_test, -1, axis = 0) # rolls y upwards

# img_roll_right = np.roll(state_test, 1, axis = 1) # rolls x right
# img_roll_left = np.roll(state_test, -1, axis = 1) # rolls x left

# #to reach the diagonal corners:
# img_roll_left_up = np.roll(state_test, [-1, -1], axis=(0, 1)) #rolls left up 
# img_roll_left_down = np.roll(state_test, [1, -1], axis=(0, 1)) #rolls left down
# #....

# print(img_roll_down)
# print()
# print(img_roll_up)
# print()
# print()
# print(img_roll_right)
# print()
# print(img_roll_left)
# print()
# print()
# print(img_roll_left_up)
# print()
# print(img_roll_left_down)

# number_neighbours_test = img_roll_down + img_roll_up + img_roll_down
# print(number_neighbours_test)
