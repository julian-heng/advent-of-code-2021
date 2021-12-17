#!/usr/bin/env python3

import re
import sys


def main(fname):
    with open(fname) as f:
        r = re.findall("[xy]=(-?\d+)..(-?\d+)", f.read())
        tx, ty = [tuple(int(j) for j in i) for i in r]
    print(solve1(tx, ty))
    print(solve2(tx, ty))


def solve1(tx, ty):
    return ((abs(ty[0]) - 1) * abs(ty[0])) // 2


def solve2(tx, ty):
    r = set()
    for _xd in range(max(tx) + 1):
        for _yd in range(-abs(min(ty)), abs(min(ty))):
            xd = _xd
            yd = _yd
            x = 0
            y = 0
            while x <= tx[1] and y >= ty[0]:
                if tx[0] <= x <= tx[1] and ty[0] <= y <= ty[1]:
                    r.add((_xd, _yd))
                    break
                x += xd
                y += yd
                xd -= 1 if xd > 0 else 0
                yd -= 1
    return len(r)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
