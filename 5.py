# -*- coding: utf-8 -*-

"""
Smallest multiple
==========================

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import time

def smallest(a, b):
    m, n = (a, b) if a > b else (b, a)
    
    while n != 0:
        r = m % n
        m, n = n, r

    return a / m * b


def find():
    n = 1
    for i in range(1, 21):
        n = smallest(n, i)
    return n


if __name__ == '__main__':
    start = time.time()
    s = find()
    print s, time.time() - start
