#!/usr/bin/env python3

import sys

from operator import add, sub
from itertools import chain, combinations, product
from collections import Counter, deque


def main(fname):
    with open(fname) as f:
        s = f.read()
    sc = process_input(s)
    pts, ds = solve1(sc)
    print(pts)
    print(solve2(ds))


def process_input(s):
    sc = [tuple(tuple(int(k) for k in j.split(","))
                             for j in i.splitlines()[1:])
                             for i in s.split("\n\n")]
    return sc


def solve1(sc):
    pts = set(sc[0])
    r = deque(sc[1:])
    sc = [(0, 0, 0)]
    while r:
        scn = r.popleft()
        scv, npts = find(pts, scn)
        if scv:
            pts = pts.union(npts)
            sc.append(scv)
        else:
            r.append(scn)
    return len(pts), sc


def solve2(sc):
    return max(sum(pt_mag(pt1, pt2)) for pt1, pt2 in combinations(sc, 2))


def find(pts, sc):
    for rsc in cube24(sc):
        n = Counter(pt_sub(pt1, pt2) for pt1, pt2 in product(pts, rsc))
        d, c = n.most_common()[0]
        if c >= 12:
            return d, {pt_add(pt, d) for pt in rsc}
    return None, None


def pt_op(p1, p2, f):
    return tuple(f(a, b) for a, b in zip(p1, p2))


def pt_add(p1, p2):
    return pt_op(p1, p2, add)


def pt_sub(p1, p2):
    return pt_op(p1, p2, sub)


def pt_mag(p1, p2):
    return pt_op(p1, p2, lambda a, b: abs(sub(a, b)))


def cube24(va):
    yield va
    pp = ((0, 1, 2), (1, 2, 0), (2, 0, 1))
    sp = ((1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1))
    pn = ((0, 2, 1), (1, 0, 2), (2, 1, 0))
    sn = ((-1, 1, 1), (1, -1, 1), (1, 1, -1), (-1, -1, -1))
    for p, s in chain(product(pp, sp), product(pn, sn)):
        yield [tuple(i[p[j]] * s[j] for j in range(3)) for i in va]


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
