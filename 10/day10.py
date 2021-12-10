#!/usr/bin/env python3

import sys

from functools import reduce


def main(fname):
    with open(fname) as f:
        l = [[j for j in i] for i in f.read().splitlines()]
    s, l2 = solve1(l)
    print(s)
    print(solve2(l2))


def solve1(l):
    t1 = {")": "(", "]": "[", "}": "{", ">": "<"}
    t2 = {v: k for k, v in t1.items()}
    t3 = {")": 3, "]": 57, "}": 1197, ">": 25137}
    l2 = []
    s = 0
    for i in l:
        t = []
        z = True
        for j in i:
            if j in t1.values():
                t.append(j)
            if j in t3.keys() and t.pop() != t1[j]:
                s += t3[j]
                z = False
                break
        if z:
            l2.append([t2[j] for j in reversed(t)])
    return s, l2


def solve2(l):
    t = {")": 1, "]": 2, "}": 3, ">": 4}
    s = [reduce(lambda s, j: (s * 5) + t[j], i, 0) for i in l]
    return sorted(s)[(len(s) - 1) // 2]


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
