#!/usr/bin/env python3

from sys import stdin
import re

def part1(pairs: list[tuple]) -> int:
    return sum((la <= ra and rb <= lb) or (ra <= la and lb <= rb) for la, lb, ra, rb in pairs)

def part2(pairs: list[tuple]) -> int:
    return sum((la <= ra <= lb) or (ra <= la <= rb) for la, lb, ra, rb in pairs)

def main():
    print('Day 04')

    data = stdin.read().split('\n')
    pairs = [tuple(map(int, re.split(r',|-', pair))) for pair in data]

    print(part1(pairs))
    print(part2(pairs))

if __name__ == '__main__':
    main()
