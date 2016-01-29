#!/usr/bin/env python

"""
bio-2014-1-2.py: Sample solution for question 2 on
the 2014 British Informatics Olympiad Round One exam

Loops
"""

__author__  = "Pratheek Nagaraj"
__date__    = "12 January 2016"

"""
This problem is best solved with some good representation
and then a simple algorithm to find loops and perform the
couting. We represent the different types of tiles by
the endpoints of the line (up, bottom, left, right). Then 
to find a loop we simply start at one tile and follow the
outgoing edges to other tiles, and not backtrack our steps.
If we have a loop then it'll be more than 2 tiles traversed
and we will end up at the starting position. We need to
be mindful of edge cases. We perform a loop check at each
cell to do the counting to avoid any double counting.
"""

tiles_green = {
    1: [(-1, 0),( 1, 0)],
    2: [( 0,-1),( 0, 1)],
    3: [( 1, 0),( 0, 1)],
    4: [(-1, 0),( 0, 1)],
    5: [(-1, 0),( 0,-1)],
    6: [( 1, 0),( 0,-1)]
}

tiles_red = {
    2: [(-1, 0),( 1, 0)],
    1: [( 0,-1),( 0, 1)],
    5: [( 1, 0),( 0, 1)],
    6: [(-1, 0),( 0, 1)],
    3: [(-1, 0),( 0,-1)],
    4: [( 1, 0),( 0,-1)]
}

size = int(raw_input())
grid = []
for _ in xrange(size):
    line = [int(i) for i in raw_input().strip().split()]
    grid.append(line)

def get_score(tiles):
    score = 0
    for i in xrange(size):
        for j in xrange(size):
            if is_valid_loop(tiles, (i,j)):
                score += 1
    return score

def is_valid_loop(tiles, start):
    visited = set()
    agenda = [start]
    while len(agenda) > 0:
        cur = agenda.pop(0)
        visited.add(cur)
        x,y = cur

        # Ensure that the loop stays in the grid
        if 0 <= x < size and 0 <= y < size:    
            moves = tiles[grid[x][y]]
            for move in moves:
                pos = (x+move[1], y+move[0])

                # Have we returned to start cell and is the loop larger than 2
                if pos == start and len(visited) > 2:
                    return True
                if pos not in visited:
                    agenda.append(pos)
                    break
        else:
            return False
    return False

print get_score(tiles_red), get_score(tiles_green)