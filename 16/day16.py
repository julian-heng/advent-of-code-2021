#!/usr/bin/env python3

import sys

from itertools import takewhile
from functools import reduce


def main(fname):
    with open(fname) as f:
        s = f.read().splitlines()[0]
        s = "".join(bin(int(i, 16))[2:].zfill(4) for i in s)
    l, _ = process_input(s)
    print(solve1(l))
    print(solve2(l))


def process_input(s):
    if not "1" in s:
        return [], ""
    v, s = int(s[:3], 2), s[3:]
    pt, s = int(s[:3], 2), s[3:]
    r = []
    ps = []
    if pt == 4:
        n = pt + 1
        sp, s = s[:n], s[n:]
        while sp[0] == "1":
            ps.append(sp)
            sp, s = s[:n], s[n:]
        if sp:
            ps.append(sp)
    else:
        lt, s = 15 if s[0] == "0" else 11, s[1:]
        l, s = int(s[:lt], 2), s[lt:]
        if lt == 15:
            sp, s = s[:l], s[l:]
            while sp:
                _r, sp = process_input(sp)
                r.append(_r)
        else:
            for _ in range(l):
                _r, s = process_input(s)
                r.append(_r)
    r.append((v, pt, int("".join(i[1:] for i in ps), 2) if ps else 0))
    return r, s


def solve1(l):
    if isinstance(l, tuple):
        return l[0]
    return sum(solve1(i) for i in l)


def solve2(l):
    (_, t, v), l = l[-1], l[:-1]
    if t == 0:
        return sum(solve2(i) for i in l)
    elif t == 1:
        return reduce(lambda a, b: a * b, (solve2(i) for i in l))
    elif t == 2:
        return min(solve2(i) for i in l)
    elif t == 3:
        return max(solve2(i) for i in l)
    elif t == 4:
        return v
    elif t == 5:
        return int(solve2(l[1]) < solve2(l[0]))
    elif t == 6:
        return int(solve2(l[0]) < solve2(l[1]))
    elif t == 7:
        return int(solve2(l[0]) == solve2(l[1]))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
