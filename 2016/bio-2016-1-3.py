#!/usr/bin/env python

"""
bio-2016-1-3.py: Sample solution for question 3 on
the 2016 British Informatics Olympiad Round One exam

Prime Connections
"""

__author__  = "Pratheek Nagaraj"
__date__    = "12 January 2016"

"""
The strategy for this problem is to create a tree from
the starting numer to the ending number. We precompute
the powers of 2 which are allowed. Then we perform a 
breadth-first search from start to end. Valid moves
are from the current number to one that is a power of 2
away (plus or minus) and is prime. We maintain a visited
set of values so that we don't repeat numbers (as we are
performing a BFS we will necessarily find the shortest 
path). 
"""

# NOTE: This program takes some time to run in the larger
# test cases, one needs to use a better algorithm to achieve 
# the less than one second bound from the rules.

import math
import heapq

primes = set([])

def is_prime(a):
    '''Function to determine is a number is prime,
    also maintains a cache of current primes found'''

    if a in primes:
        return True
    yes = a > 1 and all(a % i for i in xrange(2, int(math.pow(a,0.5))+1))
    if yes:
        primes.add(a)
    return yes

# Take in input
parts = raw_input().split()

upper_limit = int(parts[0])
start = int(parts[1])
end = int(parts[2])



# Precompute powers of two
differences = [2**x for x in xrange(0,25)]

def shortest_path(start, end, upper_limit):
    visited = set([])

    # Maintain a tuple for (number, path length)
    agenda = [(start,1,[start])]

    # Perform a breadth first search
    while len(agenda) > 0:
        cur, length, path = agenda.pop(0)

        # Do not repeat visited numbers
        if cur in visited:
            continue

        visited.add(cur)
        
        for diff in differences:
            top = cur + diff
            bottom = cur - diff
            
            # Found the shortest path
            if top == end or bottom == end:
                tot = path + [end]
                for i in tot:
                    print bin(i), i
                return length + 1

            # Prune for range and if it is prime
            if top <= upper_limit and is_prime(top):
                agenda.append((top,length+1,path+[top]))
            if bottom >= 2 and is_prime(bottom):
                agenda.append((bottom,length+1,path+[bottom]))

print shortest_path_heuristic(start, end, upper_limit)
