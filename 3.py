"""
Largest prime factor
====================

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import time

def find(n):
    while n % 2 == 0:
        n = n / 2

    p = 1
    while n != 1:
        p += 2
        while n % p == 0:
            n = n / p
    return p


if __name__ == '__main__':
    start = time.time()
    lp = find(600851475143)
    print lp, time.time() - start
