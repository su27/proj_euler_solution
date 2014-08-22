# -*- coding: utf-8 -*-

"""
Largest palindrome product
==========================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time

def find():
    p = 0
    for i in xrange(100, 1000):
        for j in xrange(i, 1000):
            x = i * j
            strx = str(x)
            if strx == ''.join(list(reversed(strx))):
                p = max(p, x)
    return p


if __name__ == '__main__':
    start = time.time()
    lp = find()
    print lp, time.time() - start
