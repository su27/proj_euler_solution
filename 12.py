import time
from operator import mul
from itertools import count


def prime_factors(n):
    while n % 2 == 0:
        yield 2
        n /= 2

    while n % 3 == 0:
        yield 3
        n /= 3

    p = 1
    while n != 1:
        p += 4
        while n % p == 0:
            yield p
            n /= p

        p += 2
        while n % p == 0:
            yield p
            n /= p


def find_factors_num(n):
    prime_nums = [1]
    last_p = 0
    for p in prime_factors(n):
        if p == last_p:
            prime_nums[-1] += 1
        else:
            prime_nums.append(2)
            last_p = p

    return reduce(mul, prime_nums)


def do_find():
    res = 1
    for i in count(start=2):
        res += i
        factors_num = find_factors_num(res)
        if factors_num > 500:
            return res


if __name__ == '__main__':
    start = time.time()
    res = do_find()
    print res, time.time() - start
