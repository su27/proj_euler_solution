# -*- coding: utf-8 -*-

"""
Sum square difference
==========================

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

import time

def find():
    s = 0
    for i in xrange(1, 101):
        for j in xrange(1, 101):
            if i != j:
                s += i * j
    return s


if __name__ == '__main__':
    start = time.time()
    print find(), time.time() - start
