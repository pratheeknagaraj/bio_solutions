#!/usr/bin/env python

"""
bio-2015-1-1.py: Sample solution for question 1 on
the 2015 British Informatics Olympiad Round One exam

Block Palindromes
"""

__author__  = "Pratheek Nagaraj"
__date__    = "12 January 2016"

"""
The approach here is recursive and we take advantage of
python's lists in order to make the reversal and splicing
operations easier. For each correct palindrome the
count is propogated to the top through the recursive calls.
"""

def recursive_count(left, right):
    if left == right == "":
        return 1

    size = len(left)
    count = 1

    for end in xrange(size):
        left_part = left[:end+1]
        right_part = right[:end+1]
        if left_part == right_part[::-1]:
            count += recursive_count(left[end+1:], right[end+1:])

    return count

def block_palindromes(word):
    length = len(word)

    left = word[:length/2]
    right = word[length/2+1:]
    if length % 2 == 0:
        right = word[length/2:]
    
    right = right[::-1]
    return recursive_count(left, right) - 1
    
in1 = raw_input()
print block_palindromes(in1)

