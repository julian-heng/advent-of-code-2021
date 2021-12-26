#!/usr/bin/env python3

import sys

from functools import reduce
from itertools import product


def main(fname):
    with open(fname) as f:
        _a, _b = [i.splitlines() for i in f.read().split("\n\n")]
        alg = [i == "#" for i in _a[0]]
        im = {(i, j) for i, r in enumerate(_b)
                     for j, c in enumerate(r) if c == "#"}
    print(solve(alg, im, n=2))
    print(solve(alg, im, n=50))


def solve(alg, im, n=1):
    for _n in range(n):
        on = (_n % 2) == 0
        _y = [y for y, _ in im]
        _x = [x for _, x in im]
        _min = min(min(_y), min(_x))
        _max = max(max(_y), max(_x))
        _im = set()
        for y, x in product(range(_min-2, _max+2), repeat=2):
            a = [(i in im) == on for i in adj(y, x)]
            s = reduce(lambda i, j: (i << 1) + int(j), a)
            if alg[s] != on:
                _im.add((y, x))
        im = _im
    return len(im)


def adj(y, x):
    for _y, _x in product(range(y-1, y+2), range(x-1, x+2)):
        yield _y, _x


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
