#!/usr/bin/env python3

import sys


def main(fname):
    with open(fname) as f:
        l = list(map(int, f.read().splitlines()))
        ll = list(map(sum, zip(l, l[1::], l[2::])))
    print(len(solve(l)))
    print(len(solve(ll)))


def solve(l):
    return list(filter(lambda a: a > 0, map(lambda a, b: b - a, l, l[1:])))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
