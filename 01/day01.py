#!/usr/bin/env python3


def main():
    with open("input") as f:
        l = list(map(int, f.read().splitlines()))
        ll = list(map(sum, zip(l, l[1::], l[2::])))
    print(len(solve(l)))
    print(len(solve(ll)))


def solve(l):
    return list(filter(lambda a: a > 0, map(lambda a, b: b - a, l, l[1:])))


if __name__ == "__main__":
    main()
