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
from math import log, sqrt

def find(m):
    n = int(m * log(m))
    sq = int(sqrt(n)) + 1
    candi = [i for i in range(5, n, 2) if i % 3 != 0]
    primes = [2, 3]
    while 1:
        p = candi.pop(0)
        primes.append(p)
        pk = p
        while pk <= n:
            if pk in candi:
                candi.remove(pk)
            pk += p
        if p > sq:
            break

    allp = primes + candi
    return len(allp), allp[-1], allp[10001]


def find2(m):
    def not_prime(k):
        for i in xrange(3, int(sqrt(k))+1, 2):
            if k % i == 0:
                return True

    p = 3
    num = 1
    while num < m:
        if not not_prime(p):
            num += 1
        p += 2
    return p - 2


if __name__ == '__main__':
    start = time.time()
    print find2(10001)
    print time.time() - start
