#!/usr/bin/env python3

import sys

import math
from functools import reduce
from itertools import permutations


def main(fname):
    with open(fname) as f:
        l = [eval(i) for i in f.read().splitlines()]
    print(solve1(l))
    print(solve2(l))


def solve1(l):
    return sfn_magnitude(reduce(sfn_add, sfn_copy(l)))


def solve2(l):
    return max(solve1(i) for i in permutations(l, 2))


def sfn_add(a, b):
    r = [a, b]
    c = True
    while c:
        c, _, r, _ = sfn_explode(r)
        if c:
            continue
        c, r = sfn_split(r)
    return r


def sfn_explode(a, n=0):
    if not isinstance(a, list):
        return False, None, a, None
    if n == 4:
        return True, a[0], 0, a[1]
    la, ra = a
    c, l, la, r = sfn_explode(la, n + 1)
    if c:
        return True, l, [la, sfn_add_left(ra, r)], None
    c, l, ra, r = sfn_explode(ra, n + 1)
    if c:
        return True, None, [sfn_add_right(la, l), ra], r
    return False, None, a, None


def sfn_split(a):
    if not isinstance(a, list):
        if a >= 10:
            return True, [a // 2, (a // 2) + (a % 2)]
        return False, a
    la, ra = a
    c, la = sfn_split(la)
    if c:
        return True, [la, ra]
    c, ra = sfn_split(ra)
    return c, [la, ra]


def sfn_add_left(a, n):
    if n is None:
        return a
    if not isinstance(a, list):
        return a + n
    return [sfn_add_left(a[0], n), a[1]]


def sfn_add_right(a, n):
    if n is None:
        return a
    if not isinstance(a, list):
        return a + n
    return [a[0], sfn_add_right(a[1], n)]


def sfn_magnitude(a):
    if not isinstance(a, list):
        return a
    return (sfn_magnitude(a[0]) * 3) + (sfn_magnitude(a[1]) * 2)


def sfn_copy(a):
    if not isinstance(a, list):
        return a
    return [sfn_copy(i) for i in a]


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
