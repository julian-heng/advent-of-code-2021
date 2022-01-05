#!/usr/bin/env python3

import sys


def main(fname):
    with open(fname) as f:
        s = f.read()
    sf, ef, sfmax, efmax = process_input(s)
    print(solve(sf, ef, sfmax, efmax))


def process_input(s):
    l = s.splitlines()
    sfmax = len(l)
    efmax = len(l[0])
    sf = set()
    ef = set()
    h = (((r, c), vc) for r, vr in enumerate(l)
                      for c, vc in enumerate(vr) if vc != ".")
    for (r, c), v in h:
        (sf if v == "v" else ef).add((r, c))
    return sf, ef, sfmax, efmax


def solve(sf, ef, sfmax, efmax):
    n = 0
    while True:
        _sf, _ef = _step(sf, ef, sfmax, efmax)
        n += 1
        if _sf == sf and _ef == ef:
            break
        sf = _sf
        ef = _ef
    return n


def _step(sf, ef, sfmax, efmax):
    _ef = {(r, (c + 1) % efmax
        if (r, (c + 1) % efmax) not in sf
            and (r, (c + 1) % efmax) not in ef else c)
        for r, c in ef}
    _sf = {((r + 1) % sfmax
        if ((r + 1) % sfmax, c) not in _ef
            and ((r + 1) % sfmax, c) not in sf else r, c)
        for r, c in sf}
    return _sf, _ef


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
