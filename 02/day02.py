#!/usr/bin/env python3

import sys


def main(fname):
    with open(fname) as f:
        l = map(str.split, f.read().splitlines())
        l = map(lambda i: (i[0][0], int(i[1])), l)
        l = list(l)
    print(solve1(l))
    print(solve2(l))


def solve1(l):
    x = 0
    y = 0
    for d, m in l:
        if d == "f":
            x += m
        elif d == "d":
            y += m
        elif d == "u":
            y -= m
    return x * y


def solve2(l):
    a = 0
    x = 0
    y = 0
    for d, m in l:
        if d == "f":
            x += m
            y += m * a
        elif d == "d":
            a += m
        elif d == "u":
            a -= m
    return x * y


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
