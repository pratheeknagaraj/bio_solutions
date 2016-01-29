#!/usr/bin/env python

"""
bio-2014-1-2.py: Sample solution for question 3 on
the 2014 British Informatics Olympiad Round One exam

Unlock
"""

__author__  = "Pratheek Nagaraj"
__date__    = "27 January 2016"

"""
This is a tricky problem as the space of solutions is large. One
approach was to solve a system of modular linear equations. 
The concern was a non-invertible matrix and so a row reduction
approach often left inconsistent solutions. The taken approach uses
a branch and bound approach where we bound ourselves to the time
limit if the flag is set and otherwise branch on button press
combinations. Naively we could ahve 3^25 combinations. However, 
since we are going alphabetically and we can look at the result of
button presses we can apply actions to a grid.

We use a Keypad class to store a state of the key pad the operations
performed as well as methods to perform actions. The ButtonCombination
class simply generates the combinations of presses we need. Then the 
remaining methods perform the logic of the branching search algorithm.

Note that with the 5 second time restriction all test cases except the
first pass (later alphabetically), whereas the without the timelimit
all answers are correct, though impossibility takes much longer to report.

This solution is based off of: 
https://github.com/TomHarling/BIO_Solutions/tree/master/BIO_13_3
"""

import string
import copy
import time

in_cmd = list(raw_input().strip())

time_start = time.time()
time_flag = True
time_out = 4.5

## ========== Keypad ==============

class Keypad:


    def __init__(self, lighting_string=None, keypad=None):

        self.dirs = [(0,0),(-1,0),(0,-1),(1,0),(0,1)]
        if keypad == None:
            self.lighting_string = lighting_string

        self.setup_keypad(keypad)

    # Setup the keypad based off initial string or previous keypad
    def setup_keypad(self,keypad=None):
        self.state = [[0 for i in xrange(5)] for j in xrange(5)]
        self.times_pressed = [[0 for i in xrange(5)] for j in xrange(5)]
        self.can_press = [[False for i in xrange(5)] for j in xrange(5)]

        for row in xrange(5):
            for col in xrange(5):
                if keypad == None:
                    self.state[row][col] = self.get_initial_state(row, col)
                    self.times_pressed[row][col] = 0
                    self.can_press[row][col] = True
                else:
                    self.state[row][col] = keypad.state[row][col]
                    self.times_pressed[row][col] = keypad.times_pressed[row][col]
                    self.can_press[row][col] = keypad.can_press[row][col]

    # Determine the off, dim, bright setting of a button
    def get_initial_state(self, row, col):
        lower = string.lowercase
        upper = string.uppercase

        pos = row*5 + col
        l, u = lower[pos], upper[pos]
        if l in self.lighting_string:
            return 1
        elif u in self.lighting_string:
            return 2
        return 0

    def unlocked(self):
        for row in xrange(5):
            for col in xrange(5):
                if self.state[row][col] != 0:
                    return False
        return True

    # Determine the number of times to press to turn off
    def times_to_press(self, row, col):
        return (3 - self.state[row][col]) % 3

    def print_button_presses(self):
        out = ""
        for row in xrange(5):
            for col in xrange(5):
                pos = row*5 + col
                if self.times_pressed[row][col] == 1:
                    out += string.lowercase[pos]
                elif self.times_pressed[row][col] == 2:
                    out += string.uppercase[pos]
        print out 

    # Press a series of buttons
    def press_combination(self, row, col, counts):
        for count, d in zip(counts, self.dirs):
            x = row + d[0]
            y = col + d[1]
            if not self.press_button(x, y, count, False):
                return False
        return True

    # Press a button and check if it is a valid press
    def press_button(self, row, col, count, multiple_presses):
        if not self.in_range(row, col):
            return count == 0
        if not self.can_press[row][col]:
            return count == 0

        for d in self.dirs:
            x = row + d[0]
            y = col + d[1]
            
            if self.in_range(x,y):
                self.state[x][y] = (self.state[x][y] + count) % 3

        self.times_pressed[row][col] = count
        self.can_press[row][col] = multiple_presses
        return True

    def is_off(self, row, col):
        return self.state[row][col] == 0

    def in_range(self, row, col):
        return 0 <= row < 5 and 0 <= col < 5


## ========== Combinations ==============

class ButtonCombination:

    def __init__(self):
        self.combinations = {1: [], 2: []}
        self.generate_combinations([0]*5, 0, 0)

    # Generate button pressing combinations and store in map
    # middle change times -> button press counts (up,down,left,right,center)
    def generate_combinations(self, button_presses, index, middle):
        for times_pressed in xrange(3):
            button_presses[index] = times_pressed

            if index == 4:
                presses = (middle + times_pressed) % 3
                if presses != 0:
                    self.combinations[presses].append(copy.copy(button_presses))
            else:
                self.generate_combinations(button_presses, index + 1, middle + times_pressed)

    def get(self,i):
        return self.combinations[i]

button_combinations = ButtonCombination()

## ========== Unlocker ==============

def get_presses_to_unlock(lighting_string):
    stack = []
    stack.append(Keypad(lighting_string=lighting_string))

    while not solution_found(stack):
        push_child_keypads(stack)

def push_child_keypads(stack):
    keypad = stack.pop()
    for row in xrange(5):
        for col in xrange(5):
            if not keypad.is_off(row, col):
                push_ways_to_turn_off(row, col, keypad, stack)
                return 

def push_ways_to_turn_off(row, col, keypad, stack):
    # copy the current keypad and produce button presses for the next cell
    for combination in button_combinations.get(keypad.times_to_press(row, col)):
        child_keypad = Keypad(keypad=keypad)
        if child_keypad.press_combination(row, col, combination):
            stack.append(child_keypad)

def solution_found(stack):
    if len(stack) == 0 or \
        (time_flag and (time.time() - time_start > time_out)):
        print "IMPOSSIBLE"
        return True
    
    keypad = stack[-1]
    if keypad.unlocked():
        keypad.print_button_presses()
        return True
    
    return False

get_presses_to_unlock(in_cmd)