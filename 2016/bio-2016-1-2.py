#!/usr/bin/env python

"""
bio-2016-1-2.py: Sample solution for question 2 on
the 2016 British Informatics Olympiad Round One exam

Migration
"""

__author__  = "Pratheek Nagaraj"
__date__    = "12 January 2016"

"""
This question deals with simulation of a grid of cells
that overflow once a capacity has been reached. The tricky
part is that it is an infinite grid of cells, but we only
have to output the 5x5 region we are centered on. We cannot
a priori represent all cells in the infinite grid and we must
have some mechanism to account for cells outside the 5x5
region as an overflow outside the centered region can flow
into the 5x5 region.

The approach implemented here is to at runtime create the 
additional neighboring cells if they contain person as a
result of a flow outside the 5x5 region. We maintain a 
2-dimensional array/list for the 5x5 region but store it
in a dictionary, so when new cells outside the region are
important we can look them up by the coordinates in the 
dictionary.
"""

grid = {}

# create starting cells

for i in xrange(1,6):
    for j in xrange(1,6):
        tup = (i,j)
        grid[tup] = 0

# handle necessary input

row1 = raw_input()
row2 = raw_input()

s1 = row1.split()
p = int(s1[0])
s = int(s1[1])
n = int(s1[2])

s2 = row2.split()
seq = [int(x) for x in s2]

if len(seq) != s:
    print "Sequence Length does not match"

def get_tup(pos):
    '''Get the (x,y) tuple position from the 1-25 value'''

    y = (pos-1) / 5 + 1
    x = pos % 5
    if x == 0:
        x = 5
    tup = (x,y)
    return tup

def make_step(tup):
    '''Place a person at the indicated (x,y) tuple position'''

    if tup not in grid:
        grid[tup] = 0
    grid[tup] += 1
    if grid[tup] == 4:
        flood()

def add_tup(tup1, tup2):
    '''Compute a new tuple position as a result of adding tup1 and tup2'''

    return (tup1[0] + tup2[0], tup1[1] + tup2[1])

def flood():
    '''If there is an overflow, move people to adjacent cells,
    do so while there is at least 4 people in any cell'''

    # directions which people migrate out of a cell
    deltas = [(0,1), (1,0), (-1,0), (0,-1)]

    need_to_flood = True
    while need_to_flood:
        need_to_flood = False
        for tup, count in grid.items():
            if count >= 4:              # need to flood a cell
                need_to_flood = True
                
                for d in deltas:
                    new_tup = add_tup(tup, d)
                    if new_tup not in grid:
                        grid[new_tup] = 0
                    grid[new_tup] += 1
                grid[tup] -= 4

def print_grid():
    '''Print the grid'''

    for y in xrange(1,6):
        line = ""
        for x in xrange(1,6):
            line += str(grid[(x,y)])
        print line

pos = p
for step in xrange(n):
    tup = get_tup(pos)
    make_step(tup)

    num = step % len(seq)
    pos = (pos + seq[num]) % 25
    if pos == 0:
        pos = 25

print_grid()
