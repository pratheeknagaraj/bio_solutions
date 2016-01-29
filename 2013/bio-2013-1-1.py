#!/usr/bin/env python

"""
bio-2013-1-1.py: Sample solution for question 1 on
the 2013 British Informatics Olympiad Round One exam

Watching the Clock
"""

__author__  = "Pratheek Nagaraj"
__date__    = "25 January 2016"

"""
This is a straightforward and simple simulation question.
We simply loop until we have a coincident time and output
the time correctly formatted.
"""

f1, f2 = [int(i) for i in raw_input().strip().split()]

c1 = 0
c2 = 0

while True:
    c1 += 60 + f1
    c2 += 60 + f2
    c1 = c1 % (24*60)
    c2 = c2 % (24*60)
    if c1 == c2:
        break

print "%02d:%02d" % (c1/60, c1%60)