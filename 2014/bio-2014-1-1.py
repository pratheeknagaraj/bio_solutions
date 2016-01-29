#!/usr/bin/env python

"""
bio-2014-1-1.py: Sample solution for question 1 on
the 2014 British Informatics Olympiad Round One exam

Lucky Numbers
"""

__author__  = "Pratheek Nagaraj"
__date__    = "25 January 2016"

"""
This is simply an implemenation based problem. We first
generate the list of lucky numbers via the algorithm
provided and then use a binary search to find the 
corresponding lower and greater elements.
"""

# Generate luck numbers list

vals = range(1,11000,2)
complete = False
cur_index = 1
cur = None
while not complete:
    cur = vals[cur_index]
    
    if len(vals) < cur:
        break

    end_index = cur*(len(vals)/cur)-1
    for i in xrange(end_index, -1, -cur):
        vals.pop(i)
    cur_index += 1

# Find the lucky numbers

def find_less_greater(val):
    pos = binary_search(0, len(vals)-1, val)
    if vals[pos] == val:
        return vals[pos-1], vals[pos+1]
    if vals[pos] < val:
        return vals[pos], vals[pos+1]
    return vals[pos-1], vals[pos]

def binary_search(start, end, val):
    if start >= end:
        return start

    mid_pos = (end-start)/2 + start
    mid_val = vals[mid_pos]
    if val < mid_val:
        return binary_search(start, mid_pos-1, val)
    elif val > mid_val:
        return binary_search(mid_pos+1, end, val)
    return mid_pos

def lucky_numbers(val):
    lower, upper = find_less_greater(val)
    print lower, upper
    return (lower, upper) 

in1 = raw_input()
lucky_numbers(int(in1))