# -*- coding: utf-8 -*-

"""
Special Pythagorean triplet
"""

import time

def find():
    for a in xrange(1, 500):
        b = (1000.0 - a + a*a/(1000.0-a)) / 2
        if int(b) == b:
            b = int(b)
            c = 1000 - a - b
            return a, b, c, a*b*c


if __name__ == '__main__':
    start = time.time()
    print find()
    print time.time() - start, "seconds"
