#!/usr/bin/env python3

import sys


def main(fname):
    with open(fname) as f:
        l = [tuple(tuple(set(k) for k in j.split()) for j in i.split(" | "))
                for i in f.read().strip().splitlines()]
    print(solve1(l))
    print(solve2(l))


def solve1(l):
    _l = (k for j in (i[1] for i in l) for k in j)
    return len(list(filter(lambda i: len(i) in (2, 4, 3, 7), _l)))


def solve2(l):
    s = []
    r = [set()] * 10
    for k, v in l:
        r[1] = next(i for i in k if len(i) == 2)
        r[4] = next(i for i in k if len(i) == 4)
        r[7] = next(i for i in k if len(i) == 3)
        r[8] = next(i for i in k if len(i) == 7)
        x = [i for i in k if len(i) == 5]
        y = [i for i in k if len(i) == 6]

        r[9], y = find_filter(lambda i: i > r[4], y)
        r[0], y = find_filter(lambda i: i > r[7], y)
        r[3], x = find_filter(lambda i: r[1] < i < r[9], x)
        r[5], x = find_filter(lambda i: i < r[9], x)
        r[6], y = find_filter(lambda i: i > r[5], y)
        r[2] = next(iter(x))
        s.append(int("".join(str(n) for i in v for n, j in enumerate(r)
                                               if i == j)))
    return sum(s)


def find_filter(f, l):
    r = next((i for i in l if f(i)), None)
    return r, [i for i in l if i != r] if r else l


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
