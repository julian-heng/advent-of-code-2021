#!/usr/bin/env python3

import sys

from heapq import heappop, heappush


def main(fname):
    with open(fname) as f:
        s = f.read()
    l, ll = process_input(s)
    print(solve(l))
    print(solve(ll))


def process_input(s):
    l = [[int(j) for j in i] for i in s.splitlines()]
    _l = [[i[:] for i in l]]
    for i in range(8):
        _l.append([[max(1, (c + 1) % 10) for c in r] for r in _l[-1]])
    a = list(range(10))
    ll = []
    for i in zip(a[:5], a[1:6], a[2:7], a[3:8], a[4:9]):
        for ri in range(len(l)):
            rr = []
            for j in i:
                rr += _l[j][ri]
            ll.append(rr)
    return l, ll


def solve(l):
    y1 = 0
    x1 = 0
    y2 = len(l) - 1
    x2 = len(l[0]) - 1
    q = [(0, y1, x1)]
    c = {}
    while q:
        r, y1, x1 = heappop(q)
        if y1 == y2 and x1 == x2:
            break
        for y, x in get_adjacent(l, y1, x1):
            d = r + l[y][x]
            if d < c.get((y, x), sys.maxsize):
                c[(y, x)] = d
                heappush(q, (d, y, x))
    return r


def get_adjacent(l, y, x):
    if (y - 1) >= 0:
        yield (y - 1, x)
    if (y + 1) < len(l):
        yield (y + 1, x)
    if (x - 1) >= 0:
        yield (y, x - 1)
    if (x + 1) < len(l[y]):
        yield (y, x + 1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
