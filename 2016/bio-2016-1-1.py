#!/usr/bin/env python

"""
bio-2016-1-1.py: Sample solution for question 1 on
the 2016 British Informatics Olympiad Round One exam

Promenade Fractions
"""

__author__  = "Pratheek Nagaraj"
__date__    = "12 January 2016"

"""
The approach is a recursive strategy wherein we keep track
of the most recent right and left choices in the recursive
parameters as well as the most recent promenade fraction
value as we construct the fraction parsing from left to 
right.
"""

def promenade(chars):
    # initialize to the nil fraction and no left or right choice
    top, bottom = recurse(chars, 1, 1, 1, 0, 0, 1)
    print top, "/", bottom 

def recurse(chars,top,bottom,l,m,r,s):
    # If there are no more characters, then we return the current fraction
    if len(chars) == 0:
        return (top, bottom)

    cur = chars[0]
    chars = chars[1:]

    if cur == 'L':
        # reset to the most recent left choice
        l = top
        m = bottom

        top = l + r
        bottom = m + s
        
        return recurse(chars, top, bottom, l, m, r, s)
    elif cur == 'R':
        # reset to the most recent right choice
        r = top
        s = bottom

        top = l + r
        bottom = m + s

        return recurse(chars, top, bottom, l, m, r, s)

in1 = raw_input()
promenade(in1)

