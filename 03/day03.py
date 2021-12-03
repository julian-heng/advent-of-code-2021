#!/usr/bin/env python3

import sys

from functools import reduce


def main(fname):
    with open(fname) as f:
        l = [[int(j) for j in i] for i in f.read().splitlines()]
    print(solve1(l))
    print(solve2(l))


def solve1(l):
    t = [*zip(*l)]
    s1 = [(sum(i) * 2) > len(i) for i in t]
    s2 = [not i for i in s1]
    a = reduce(lambda i, j: (i << 1) + int(j), s1)
    b = reduce(lambda i, j: (i << 1) + int(j), s2)
    return a * b


def solve2(l):
    t = [*zip(*l)]
    _a = _solve2(l, t, 0, lambda i: (sum(i) * 2) >= len(i))
    _b = _solve2(l, t, 0, lambda i: (sum(i) * 2) < len(i))
    a = reduce(lambda i, j: (i << 1) + int(j), _a)
    b = reduce(lambda i, j: (i << 1) + int(j), _b)
    return a * b


def _solve2(l, t, n, f):
    if len(l) == 1:
        return l[0]

    s = [f(i) for i in t]
    l = list(filter(lambda j: j[n] == int(s[n]), l))
    b = [*zip(*l)]
    return _solve2(l, b, n + 1, f)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
