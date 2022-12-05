#!/usr/bin/env python3

from sys import stdin
import re

def part1(pairs: list[tuple]) -> int:
    return sum((x1 <= y1 and y2 <= x2) or (y1 <= x1 and x2 <= y2) for x1, x2, y1, y2 in pairs)

def part2(pairs: list[tuple]) -> int:
    return sum((x2 >= y1) and (x1 <= y2) for x1, x2, y1, y2 in pairs)
    return sum((x1 <= y1 <= x2) or (y1 <= x1 <= y2) for x1, x2, y1, y2 in pairs)

def main():
    print('Day 04')

    data = stdin.read().split('\n')
    pairs = [tuple(map(int, re.split(r',|-', pair))) for pair in data]

    print(part1(pairs))
    print(part2(pairs))

if __name__ == '__main__':
    main()
