#!/usr/bin/env python3

import re
import sys

from collections import Counter


def main(fname):
    with open(fname) as f:
        s = f.read()
    l, ll = process_input(s)
    print(solve(l))
    print(solve(ll))


def process_input(s):
    r = r"(-?\d+)\.\.(-?\d+)"
    ll = [(i.startswith("on"),
          [tuple(map(int, j)) for j in re.findall(r, i)])
          for i in s.splitlines()]
    l = []
    for i in ll:
        _, [(x1, x2), (y1, y2), (z1, z2)] = i
        if all((-50 <= j <= 50 for j in (x1, x2, y1, y2, z1, z2))):
            l.append(i)
    return l, ll


def solve(l):
    c = Counter()
    for s, [(x1, x2), (y1, y2), (z1, z2)] in l:
        c2 = Counter()
        for (_x1, _x2, _y1, _y2, _z1, _z2), s2 in c.items():
            x3 = x1 if x1 > _x1 else _x1
            x4 = x2 if x2 < _x2 else _x2
            y3 = y1 if y1 > _y1 else _y1
            y4 = y2 if y2 < _y2 else _y2
            z3 = z1 if z1 > _z1 else _z1
            z4 = z2 if z2 < _z2 else _z2
            if x3 <= x4 and y3 <= y4 and z3 <= z4:
                c2[(x3, x4, y3, y4, z3, z4)] -= s2
        if s > 0:
            c2[(x1, x2, y1, y2, z1, z2)] += s
        c.update(c2)
        c = Counter({k: v for k, v in c.items() if v != 0})
    return sum((x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * s
            for (x1, x2, y1, y2, z1, z2), s in c.items())


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
