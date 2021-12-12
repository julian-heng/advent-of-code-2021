#!/usr/bin/env python3

import sys


def main(fname):
    with open(fname) as f:
        s = f.read()
    d = process_input(s)
    print(solve1(d))
    print(solve2(d))


def process_input(s):
    l = [i.split("-", 2) for i in s.splitlines()]
    d = dict()
    for i, j in l:
        d[i] = d.get(i, set()).union({j})
        d[j] = d.get(j, set()).union({i})
    return d


def solve1(d):
    def f(i, s):
        return (
            i != "start"
            and (
                i.islower()
                and i not in s
            ) or i.isupper()
        )
    s = ()
    v = set()
    _solve(d, "start", s, v, f)
    return len(v)


def solve2(d):
    def f(i, s):
        n = 2 - any(s.count(j) == 2 for j in s if j.islower())
        return (
            i != "start"
            and (
                i.islower() and
                s.count(i) < n
            ) or i.isupper()
        )
    s = ()
    v = set()
    _solve(d, "start", s, v, f)
    return len(v)


def _solve(d, k, s, v, f):
    s = (*s, k)
    if k == "end":
        v.add(s)
        return
    for i in filter(lambda i: f(i, s), d[k]):
        _solve(d, i, s, v, f)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
