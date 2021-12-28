#!/usr/bin/env python3

import re
import sys

from functools import lru_cache, reduce
from itertools import permutations


def main(fname):
    with open(fname) as f:
        s = [int(i) for i in re.findall(r"\d+$", f.read(), re.MULTILINE)]
    print(solve1(*s))
    print(solve2(*s))


def solve1(p1, p2):
    n = 6
    s1 = 0
    s2 = 0
    c = 0
    while s1 < 1000 and s2 < 1000:
        p1 = (p1 + n) % 10
        s1 += 10 if p1 == 0 else p1
        n -= 1
        c += 3
        if s1 >= 1000:
            break
        p2 = (p2 + n) % 10
        s2 += 10 if p2 == 0 else p2
        n -= 1
        c += 3
    return s2 * c


def solve2(p1, p2):
    return max(_solve2(p1, p2))


@lru_cache(maxsize=sys.maxsize)
def _solve2(p1, p2, s1=0, s2=0):
    if s2 >= 21:
        return 0, 1
    w1 = 0
    w2 = 0
    for m, n in ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)):
        _p1 = (p1 + m) % 10
        _s1 = s1 + (10 if _p1 == 0 else _p1)
        _w2, _w1 = _solve2(p2, _p1, s2, _s1)
        w1 += n * _w1
        w2 += n * _w2
    return w1, w2


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
