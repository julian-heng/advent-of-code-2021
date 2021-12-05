#!/usr/bin/env python3

import sys

from itertools import product, zip_longest


def main(fname):
    with open(fname) as f:
        l = process_input(f.read())
    print(solve1(l))
    print(solve2(l))


def process_input(s):
    s = (i.split(" -> ") for i in s.splitlines())
    return [tuple(tuple(int(k) for k in j.split(",")) for j in i) for i in s]


def solve1(l):
    l = filter(lambda a: a[0][0] == a[1][0] or a[0][1] == a[1][1], l)
    return _solve(l)


def solve2(l):
    return _solve(l)


def _solve(l):
    f = set()
    d = set()
    a = 0
    for i in l:
        (x1, y1), (x2, y2) = i
        xd = 1 if (x2 + 1) > x1 else -1
        yd = 1 if (y2 + 1) > y1 else -1
        xc = list(range(x1, x2 + xd, xd))
        yc = list(range(y1, y2 + yd, yd))
        n = max(len(xc), len(yc))
        xc.extend([max(xc)] * (n - len(xc)))
        yc.extend([max(yc)] * (n - len(yc)))
        for c in zip(xc, yc):
            if c in f:
                if c not in d:
                    a += 1
                    d.add(c)
            else:
                f.add(c)
    return a


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
