#!/usr/bin/env python3

import sys


def main(fname):
    with open(fname) as f:
        l = [[int(j) for j in i] for i in f.read().splitlines()]
    print(solve1(l))
    print(solve2(l))


def solve1(l, n=100):
    f = 0
    for i in range(n):
        l, c = step(l)
        f += c
    return f


def solve2(l):
    n = 0
    t = sum(len(i) for i in l)
    while True:
        n += 1
        l, c = step(l)
        if c == t:
            break
    return n


def step(l):
    c = 0
    l = [[j + 1 for j in i] for i in l]
    lf = {(y, x) for y, r in enumerate(l)
                 for x, c in enumerate(r) if c > 9}
    while lf:
        c += len(lf)
        for y, x in lf:
            for _y, _x in get_adjacent(l, y, x):
                if l[_y][_x] > 0:
                    l[_y][_x] += 1
        for y, x in lf:
            l[y][x] = 0
        lf = {(y, x) for y, r in enumerate(l)
                     for x, c in enumerate(r) if c > 9}
    return l, c


def get_adjacent(l, y, x):
    neg_y = (y - 1) >= 0
    neg_x = (x - 1) >= 0
    pos_y = (y + 1) < len(l)
    pos_x = (x + 1) < len(l[y])
    if neg_y:
        if neg_x:
            yield (y - 1, x - 1)
        yield (y - 1, x)
        if pos_x:
            yield (y - 1, x + 1)
    if neg_x:
        yield (y, x - 1)
    if pos_x:
        yield (y, x + 1)
    if pos_y:
        if neg_x:
            yield (y + 1, x - 1)
        yield (y + 1, x)
        if pos_x:
            yield (y + 1, x + 1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
