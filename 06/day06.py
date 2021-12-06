#!/usr/bin/env python3

import sys

from collections import Counter


def main(fname):
    with open(fname) as f:
        l = [int(i) for i in f.read().split(",")]
    print(solve(l, 80))
    print(solve(l, 256))


def solve(l, d):
    c = dict(sorted(Counter(l).items(), key=lambda k: k[0]))
    for _ in range(d):
        z = c.get(0, 0)
        if z > 0:
            c[9] = c.get(9, 0) + z
            c[7] = c.get(7, 0) + z
            c.pop(0)
        _c = dict()
        for k, v in c.items():
            _c[k - 1] = v
        c = _c
    return sum(c.values())


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
