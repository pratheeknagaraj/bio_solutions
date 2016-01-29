#!/usr/bin/env python

"""
bio-2015-1-3.py: Sample solution for question 3 on
the 2015 British Informatics Olympiad Round One exam

Modern Art
"""

__author__  = "Pratheek Nagaraj"
__date__    = "15 January 2016"

"""
This question requires some combinatorial understanding. 
We take in an input number and determine the number of
combinations among the remaining choices recursively
until we reach the input number.
"""

import math

# factorial method for n!/a!b!c!d!
def get_combos(remaining):
    left = sum(remaining)
    out = math.factorial(left)
    for i in remaining:
        out /= math.factorial(i)
    return out

in_cmd = [int(i) for i in raw_input().strip().split()]
avail = in_cmd[:-1]
n = in_cmd[-1]

lets = 'ABCD'

counter = 0

def recurse(count_left, avail, selected):
    total_count = 0
    for artist_index in xrange(4):
        if avail[artist_index] == 0:
            continue
        
        new_avail = avail[:]
        new_avail[artist_index] -= 1

        count = get_combos(new_avail)

        # If the number of combinations put's us over the remaining we need
        if count + total_count > count_left:
            selected.append(artist_index)
            return recurse(count_left - total_count, new_avail, selected)
        
        total_count += count

    return selected


order = recurse(n-1, avail, [])
out = ''
for elem in order:
    out += lets[elem]
print out