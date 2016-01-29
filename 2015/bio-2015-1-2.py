#!/usr/bin/env python

"""
bio-2016-1-2.py: Sample solution for question 2 on
the 2016 British Informatics Olympiad Round One exam

Battleships
"""

__author__  = "Pratheek Nagaraj"
__date__    = "15 January 2016"

"""
This question is simply an implementation. One needs to
ensure that the bounds for placement are correct and
ensure that the mathematical operations are correctly
carried out according to the specifications.
"""

grid = [[0 for i in xrange(10)] for j in xrange(10)]

ships = [4,3,3,2,2,2,1,1,1,1]
placed = []

in1 = raw_input()
a, c, m = [int(x) for x in in1.strip().split()]
r = 0

def in_bounds(x,y):
    if 0 <= x < 10 and 0 <= y < 10:
        return True
    return False

def check_if_valid(x,y):
    deltas = [(-1,-1),(-1, 0),(-1, 1),
              ( 0,-1),( 0, 0),( 0, 1),
              ( 1,-1),( 1, 0),( 1, 1)]

    for d in deltas:
        check_x = x + d[0]
        check_y = y + d[1]
        if in_bounds(check_x, check_y):
            if grid[check_x][check_y] == 1:
                return False

    return True

def try_placement(x,y,size,orientation):
    delta = (1,0)
    if orientation == 'V':
        delta = (0,1)

    for i in xrange(size):
        pos_x = x + i * delta[0]
        pos_y = y + i * delta[1]
        if not in_bounds(pos_x, pos_y) or not check_if_valid(pos_x,pos_y):
            return False

    # Valid ship placement
    for i in xrange(size):
        pos_x = x + i * delta[0]
        pos_y = y + i * delta[1]
        grid[pos_x][pos_y] = 1
    
    placed.append((x,y,orientation))
    return True

while len(ships) > 0:
    current_size = ships[0]

    r = (a * r + c) % m
    x = r % 10
    y = (r / 10) % 10

    r = (a * r + c) % m

    orientation = "H"
    if r % 2 == 1:
        orientation = "V"

    if try_placement(x,y,current_size,orientation):
        ships.pop(0)

for ship in placed:
    print ship[0], ship[1], ship[2]
