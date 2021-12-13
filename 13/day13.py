#!/usr/bin/env python3

import re
import sys


def main(fname):
    with open(fname) as f:
        s = f.read()
    c, f = process_input(s)
    print(solve1(c, f))
    print(solve2(c))


def process_input(s):
    c, f = s.split("\n\n")
    c = set(tuple(int(j) for j in i.split(",")) for i in c.splitlines())
    f = [tuple([i[0], int(i[1])]) for i in re.findall("(\w+)=(\d+)", f)]
    return c, f


def solve1(c, f):
    n = None
    l = {
        "x": lambda p: tuple([b - abs(b - p[0]), p[1]]),
        "y": lambda p: tuple([p[0], b - abs(b - p[1])]),
    }
    for a, b in f:
        for p in list(filter(lambda i: i[a == "y"] > b, c)):
            c.remove(p)
            c.add(l[a](p))
        if not n:
            n = len(c)
    return n


def solve2(c):
    _x = max(i[0] for i in c) + 1
    _y = max(i[1] for i in c) + 1
    b = [["#" if (x, y) in c else " " for x in range(_x)] for y in range(_y)]
    return "\n".join(["".join(i) for i in b])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
