#!/usr/bin/env python3

import re
import sys


def main(fname):
    with open(fname) as f:
        s = f.read()
    x = process_input(s)
    print(solve1(x))
    print(solve2(x))


def process_input(s):
    r = r"div z (-?\d+)\nadd x (-?\d+)(?:[^y]*y\s){8}(-?\d+)"
    l = tuple(tuple(int(j) for j in i) for i in re.findall(r, s))
    s = []
    x = []
    for n, (a, b, c) in enumerate(l):
        if a == 1:
            s.append((n, c))
        else:
            _n, _c = s.pop()
            x.append((n, _n, b + _c))
    return x


def solve1(x):
    r = [0] * 14
    for i, j, d in x:
        r[i] = 9 + (0 if d > 0 else d)
        r[j] = 9 - (d if d > 0 else 0)
    return int("".join(str(i) for i in r))


def solve2(x):
    r = [0] * 14
    for i, j, d in x:
        r[i] = 1 + (d if d > 0 else 0)
        r[j] = 1 - (0 if d > 0 else d)
    return int("".join(str(i) for i in r))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
