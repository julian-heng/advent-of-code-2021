#!/usr/bin/env python3

import re
import sys

from collections import Counter


def main(fname):
    with open(fname) as f:
        s = f.read()
    p, r = process_input(s)
    print(solve(p, r, 10))
    print(solve(p, r, 40))


def process_input(s):
    p, r = s.split("\n\n")
    p = Counter(("".join(i) for i in zip(p, p[1:])))
    r = dict(i.split(" -> ") for i in r.splitlines())
    return p, r


def solve(p, r, n):
    for _ in range(n):
        _p = Counter()
        for i in p.keys():
            _p[f"{i[0]}{r[i]}"] += p[i]
            _p[f"{r[i]}{i[1]}"] += p[i]
        p = _p
    c = Counter()
    for k, v in p.items():
        c[k[1]] += v
    return c.most_common()[0][1] - c.most_common()[-1][1]


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
