#!/usr/bin/env python

"""
bio-2012-1-3.py: Sample solution for question 3 on
the 2012 British Informatics Olympiad Round One exam

Number Ladder
"""

__author__  = "Pratheek Nagaraj"
__date__    = "25 January 2016"

"""
This problem involves multiple steps. We first try to 
determine whether a transition from two numbers is valid.
This is done providing two numbers to the valid_move method
which compute the difference in characters via add/remove
operations between two numbers. We store a mapping of
valid moves in a graph variable which is pickle dumped for 
easy access on future runs.

We then use Djikstra's algorithm to compute the shortest path
between any two numbers along a valid route. We use a heap
data structure to improve the computational speed of the
search algorithm.
"""

import os.path
import pickle
import heapq

s1, f1 = [int(i) for i in raw_input().strip().split()]
s2, f2 = [int(i) for i in raw_input().strip().split()]
s3, f3 = [int(i) for i in raw_input().strip().split()]

shortest_paths = {}

top = 1000

words = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

# Compute difference between two numbers via add/remove operations
def valid_move(n1, n2):
    w1 = gen_word(n1)
    w2 = gen_word(n2)
    bin1 = gen_bin(w1)
    bin2 = gen_bin(w2)
    diff = get_diff(bin1, bin2)
    return diff

def get_diff(b1, b2):
    count = 0
    for key in set(b2.keys() + b1.keys()):
        count += abs(b2.get(key,0) - b1.get(key,0))

    if count <= 5:
        return True
    return False

def gen_bin(w):
    bin1 = {}
    for i in w:
        if i not in bin1:
            bin1[i] = 0
        bin1[i] += 1
    return bin1

def gen_word(n):
    w = ''
    for digit in str(n):
        w += words[int(digit)]
    return w

# Generate graph between numbers with valid transitions
def gen_graph():
    graph = {}
    for i in range(1,top):
        for j in range(i+1,top):
            if valid_move(i,j):
                if i not in graph:
                    graph[i] = [1000,[]] 
                graph[i][1].append(j)
                if j not in graph:
                    graph[j] = [1000,[]] 
                graph[j][1].append(i)
    return graph

file_name = '3-graph.txt'
if not os.path.isfile(file_name):
    graph = gen_graph()
    pickle.dump( graph, open( file_name, "wb" ) )
graph = pickle.load( open( file_name, "rb" ) )

# Find the shortest ladder between s and f
def shortest_path(s,f):
    # Run Djikstra's

    visited = set()
    agenda = [(0,s)]
    while True:
        cost, cur = heapq.heappop(agenda)
        if cur in visited:
            continue
        visited.add(cur)
        if cur == f:
            return cost
        for neighbor in graph[cur][1]:
            if neighbor not in visited:
                heapq.heappush(agenda, (cost+1, neighbor))


print shortest_path(s1,f1)
print shortest_path(s2,f2)
print shortest_path(s3,f3)