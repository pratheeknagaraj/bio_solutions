#!/usr/bin/env python

"""
bio-2012-1-2.py: Sample solution for question 2 on
the 2012 British Informatics Olympiad Round One exam

On the Right Track
"""

__author__  = "Pratheek Nagaraj"
__date__    = "12 January 2016"

"""
This is a simulation based implementation problem. We start by
manually mapping the possible connections and storing that in an 
auxiliary file '2-config.txt'. We then have a Point class represent
each intersection with the outgoing three edges. We read in the 
starting configuration and point types and apply them to the
network of points. Then the make_step method will perform a
single step through the simulation. The Point class provides methods
to handle the access patterns of the trains and changing configuration
is contained within a Point instance.
"""

import string

class Point:

    def __init__(self,kind,letter):
        self.kind = kind
        self.letter = letter
        self.setting = 'L'

        self.left = None
        self.right = None
        self.straight = None

    def enter(self, prev):
        # Logic for a Lazy intersection point
        if self.kind == 'LAZY':
            if prev == self.left:
                self.setting = 'L'
            elif prev == self.right:
                self.setting = 'R'

            if prev == self.left or prev == self.right:
                return self.straight

            if self.setting == 'L':
                return self.left
            else:
                return self.right

        # Logic for a Flip-Flop intersection point
        elif self.kind == 'FLIP':
            if prev == self.straight:
                if self.setting == 'L':
                    self.setting = 'R'
                else:
                    self.setting = 'L'

            if prev == self.left or prev == self.right:
                return self.straight

            if self.setting == 'L':
                return self.right
            else:
                return self.left

flips = list(raw_input().strip())
current = list(raw_input().strip())
n = int(raw_input())

config_file = '2-config.txt'
f = file(config_file,'r')
lines = f.readlines()

points = {}
for line in lines:
    point, left, right, straight = line.strip().split()
    kind = "LAZY"
    if point in flips:
        kind = "FLIP"
    p = Point(kind,point)
    p.left = left
    p.right = right
    p.straight = straight
    points[point] = p

def make_step(prev, pos):
    pos_p = points[pos]
    new = pos_p.enter(prev)
    return new, pos

prev, pos = current
for i in xrange(n):
    pos, prev = make_step(prev,pos)

print prev + pos