#!/usr/bin/env python

"""
bio-2012-1-1.py: Sample solution for question 1 on
the 2012 British Informatics Olympiad Round One exam

Distinct Prime Factorisation
"""

__author__  = "Pratheek Nagaraj"
__date__    = "25 January 2016"

"""
This is a relatively simple math problem. We simply
divide into the input number by primes and keep a 
running product of the prime divisors. We work
from low to high such that we only divide primes
(since a non-prime is composed of smaller primes).
"""

import math

n = int(raw_input())

product = 1
current = 2
while n != 1 and current < (int(math.sqrt(n))+1):
    if n % current == 0:
        while n % current == 0:
            n = n / current
        product *= current
    current += 1
print product*n

