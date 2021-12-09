#!/usr/bin/env python3

import sys

from functools import reduce
from itertools import product


def main(fname):
    with open(fname) as f:
        l = [[int(j) for j in i] for i in f.read().splitlines()]
    s, c = solve1([i[:] for i in l])
    print(s)
    print(solve2([i[:] for i in l], c))


def solve1(l):
    _l = [j for i in l for j in i]
    a = min(_l)
    b = max(_l)
    for n in range(b, a, -1):
        for y, i in enumerate(l):
            for x, j in enumerate(i):
                if j == n:
                    c = get_adjacent(l, y, x)
                    if any(i[0] is not None for i in c):
                        l[y][x] = None
    return sum(j + 1 for i in l for j in i if j is not None), l


def solve2(l, c):
    _l = [j for i in l for j in i]
    a = min(_l)
    b = max(_l)
    r = []
    _c = [i[:] for i in c]
    for n in range(a, b + 1):
        for y in range(len(c)):
            for x in range(len(c[y])):
                if _c[y][x] is None:
                    continue
                r.append(basin(l, c, y, x, b, 1))
    return reduce(lambda a, b: a * b, sorted(r)[-3:])


def basin(l, c, y, x, b, n):
    z = True
    for h in range(l[y][x], b):
        _c = list(i for i in get_adjacent(l, y, x) if i[0] != 9
                                                   and abs(i[0] - h) == 1)
        if not _c:
            if z:
                z = False
            else:
                break
        for v, (_y, _x) in _c:
            z = True
            if c[_y][_x] is None:
                c[_y][_x] = l[_y][_x]
                n = 1 + basin(l, c, _y, _x, b, n)
    return n


def get_adjacent(l, y, x):
    r = []
    if (y - 1) >= 0:
        r.append((l[y - 1][x], (y - 1, x)))
    if (y + 1) < len(l):
        r.append((l[y + 1][x], (y + 1, x)))
    if (x - 1) >= 0:
        r.append((l[y][x - 1], (y, x - 1)))
    if (x + 1) < len(l[y]):
        r.append((l[y][x + 1], (y, x + 1)))
    return r


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
