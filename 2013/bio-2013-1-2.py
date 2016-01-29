#!/usr/bin/env python

"""
bio-2013-1-2.py: Sample solution for question 2 on
the 2013 British Informatics Olympiad Round One exam

Neutron
"""

__author__  = "Pratheek Nagaraj"
__date__    = "25 January 2016"

"""
This can be a tricky implementation question especially since
the rules are very particular and one has to be careful to 
follow the algorithm as specified. In addition, there are
edge cases that are mentioned (no moves available) or forced
losses that must be accounted for. The sample solution below
is a bit verbose due to the unexpected complexity that arose.
One can certainly condense the solution, but it is given
here more repetitive for elucidation. 

At every given step we first check if the player can win,
then check if the player must lose, and if not either of those
two then we perform a regular move.  A regular move may not 
work if it is the case that the selected piece or the neutron
have no position to move. Further a neutron may be moved such
that it prevents the piece from moving indicating an additional
check that is required. 
"""

import copy

p1_move = [int(i) for i in raw_input().strip().split()]
p2_move = [int(j) for j in raw_input().strip().split()]

grid = [[None for i in xrange(5)] for j in xrange(5)]

# Generate a position mapping for Black, White and the neutron piece
pos = {}
for i in xrange(1,6):
    pos[("B",i)] = (0,i-1)
    grid[0][i-1] = True
    pos[("W",i)] = (4,i-1)
    grid[4][i-1] = True
pos["N"] = (2,2)
grid[2][2] = True

turn_count = 0

# Ordered 1->8 directions which pieces or neutron must move
dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def make_step(player):
    global grid
    global pos

    # Determine piece to place
    piece = ('W',p1_move[turn_count%5])
    if player == 'B':
        piece = ('B',p2_move[turn_count%5])

    # Check if winnable
    won, new_grid, new_pos = win_game(player)
    if won:
        grid = new_grid
        pos = new_pos
        return True

    # Check if forced loss
    lost, new_grid, new_pos = lose_game(player)
    if lost:
        grid = new_grid
        pos = new_pos
        return True

    # Make a regular move
    return make_regular_move(player, piece)

def make_regular_move(player, piece):
    global grid
    global pos

    neutron_moved = False
    piece_moved = False

    # Move the Neutron
    for i in xrange(8):
        d = dirs[i]
        moved, new_grid, new_pos = valid_move(d, "N")
        if not moved:
            continue

        # Ensure that the opponent hasn't won
        opponent = 'W' if player == 'B' else 'B'
        if check_win(opponent, new_pos):
            continue

        # Ensure that the selected piece can move
        if check_cant_move(piece, new_grid, new_pos):
            continue

        grid = new_grid
        pos = new_pos
        neutron_moved = True
        break

    # Move the piece
    for i in xrange(8):
        d = dirs[i]
        moved, new_grid, new_pos = valid_move(d, piece)
        if not moved:
            continue
        grid = new_grid
        pos = new_pos
        piece_moved = True
        break

    # Return whether or not game is over
    if neutron_moved and piece_moved:
        return False

    grid = new_grid
    pos = new_pos
    return True

def check_cant_move(piece, new_grid, new_pos):
    for i in xrange(8):
        d = dirs[i]
        check_grid = copy.deepcopy(new_grid)
        check_pos = copy.deepcopy(new_pos)
        moved, _, _ = valid_move(d, piece, check_grid, check_pos)
        if moved:
            return False
    return True

def win_game(player):
    for i in xrange(8):
        d = dirs[i]
        moved, new_grid, new_pos = valid_move(d, "N")
        if not moved:
            continue
        if check_win(player, new_pos):
            return (True, new_grid, new_pos)
    return (False, False, False)

def lose_game(player):
    losable = False
    lose_grid = grid
    lose_pos = pos
    for i in xrange(8):
        d = dirs[i]
        moved, new_grid, new_pos = valid_move(d, "N")
        if not moved:
            continue
        opponent = 'W' if player == 'B' else 'B'
        if check_win(opponent, new_pos):
            if not losable:
                lose_grid = new_grid
                lose_pos = new_pos
                losable = True
        else:
            return (False, False, False)
    return (True, lose_grid, lose_pos)


def check_win(player, check_pos):
    if player == 'W' and check_pos['N'][0] == 4:
        return True
    if player == 'B' and check_pos['N'][0] == 0:
        return True
    return False

def valid_move(direction, piece, new_grid=None, new_pos=None):
    #print direction, piece
    if new_grid == None:
        new_grid = copy.deepcopy(grid)
        new_pos = copy.deepcopy(pos)
    cur_pos = new_pos[piece]
    moved = False

    while True:
        # Move a piece as far as it can go in a direction
        x,y = (cur_pos[0]+direction[0],
                   cur_pos[1]+direction[1])
        if 0 <= x < 5 and 0 <= y < 5:
            if new_grid[x][y] == None:
                new_grid[cur_pos[0]][cur_pos[1]] = None
                cur_pos = (x,y)
                new_grid[x][y] = True
                new_pos[piece] = cur_pos
                moved = True
            else:
                break
        else:
            break

    return moved, new_grid, new_pos

def print_grid():
    for i in xrange(5):
        line = ''
        for j in xrange(5):
            if grid[i][j] == True:
                # Find piece
                for key, value in pos.items():
                    if value == (i,j):
                        if key == 'N':
                            line += '*'
                        elif key[0] == 'W':
                            line += 'F'
                        else:
                            line += 'S'
            else:
                line += '.'
        print line

make_step('W')
print_grid()
print ""
make_step('B')
print_grid()
print ""
turn_count += 1

moves = 2
turn = ['W','B']
while True:
    player = turn[moves % 2]
    if make_step(player):
        break

    moves += 1
    turn_count = moves/2

print_grid()