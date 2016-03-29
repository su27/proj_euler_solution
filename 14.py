import time

def main():
    lens = {}
    MAX = 1000000
    MMAX = MAX * 10

    def check(n, now_len):

        if n > MMAX:
            return
        if lens.get(n):
            return

        lens[n] = now_len

        if n % 3 == 1 and n >= 4:
            prev_n = (n - 1) / 3
            if prev_n % 2 != 0:
                check(prev_n, now_len + 1)

        check(n * 2, now_len + 1)

    check(1, 0)

    bad = set(i for i in lens.keys() if i <= MAX)

    max_k, max_v = 0, 0
    for i in xrange(1, MAX):
        if i not in bad:
            v = process(i)
            if v > max_v:
                max_k, max_v = i, v

    print max_k, max_v

def process(n):
    l = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            l += 1
        else:
            n = n * 3 + 1
            l += 1
    return l


if __name__ == '__main__':
    st = time.time()
    main()
    print 'time:', time.time() - st
