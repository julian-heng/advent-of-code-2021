#!/usr/bin/env python3

import sys

from itertools import cycle


def main(fname):
    with open(fname) as f:
        s = f.read()
    n, b = process_input(s)
    print(solve1(n, b))
    n, b = process_input(s)
    print(solve2(n, b))


def process_input(lines):
    n, *b = lines.split("\n\n")
    n = [int(i) for i in n.split(",")]
    b = [[[int(k) for k in j.split()] for j in i.splitlines()] for i in b]
    b = [[set(j) for j in i] + [set(j) for j in [*zip(*i)]] for i in b]
    return n, b


def solve1(n, b):
    for i in n:
        for j in b:
            for k in j:
                k.discard(i)
                if not k:
                    s = sum(sum(x) for x in j[:5])
                    return s * i


def solve2(n, b):
    d = set()
    for i in n:
        for c, j in enumerate(b):
            if c in d:
                continue
            for k in j:
                k.discard(i)
                if not k:
                    d.add(c)
                    if len(d) == len(b):
                        s = sum(sum(x) for x in j[:5])
                        return s * i


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
