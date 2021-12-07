#!/usr/bin/env python3

import sys


def main(fname):
    with open(fname) as f:
        l = sorted(int(i) for i in f.read().strip().split(","))
    print(solve1(l))
    print(solve2(l))


def solve1(l):
    return _solve(l, lambda i, n: abs(i - n))


def solve2(l):
    return _solve(l, lambda i, n: (abs(i - n) * (abs(i - n) + 1)) // 2)


def _solve(l, f):
    return min(sum(f(i, n) for i in l) for n in range(min(l), max(l)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
