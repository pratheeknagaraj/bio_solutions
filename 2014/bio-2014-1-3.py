#!/usr/bin/env python

"""
bio-2014-1-3.py: Sample solution for question 3 on
the 2014 British Informatics Olympiad Round One exam

Increasing Passwords
"""

__author__  = "Pratheek Nagaraj"
__date__    = "29 January 2016"

"""
This is a combinatorics question using recursion. We use a 
counting based approach where we determine the number of combinations
using a fixed set of characters and then increment to a running sum.
If the running sum exceeds the input value then we backtrack and
recurse having fixed that chosen set of characters. We first
determine the size of our password by having a running sum of 
each password length until we exceed. 
"""

import math
import string

def combination(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

n = int(raw_input())

# Determine the number of characters in our password

passed = 0
size = 1
while True:
    size_range = combination(36,size)
    if passed + size_range >= n:
        break
    passed += size_range
    size += 1

avail = string.uppercase + ''.join([str(i) for i in range(0,10)])

# Recurse over left number of characters, only using ones after start

def recurse(start, left, chosen, build):
    if chosen == size:
        return
    total_count = 0
    for i in xrange(start,36):
        count = combination(36-i-1, size-chosen-1)
        if total_count + count >= left:
            build.append(i)
            recurse(i+1, left-total_count, chosen+1, build)
            break
        total_count += count
    return build

indicies = recurse(0, n - passed, 0, [])
out = "".join([avail[i] for i in indicies])
print out
