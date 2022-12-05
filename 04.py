#!/usr/bin/env python3

from sys import stdin

def part1(bags: list) -> int:
    return None

def part2(groupedBags: list) -> int:
    return None

def main():
    print('Day 04')

    data = stdin.read().split('\n')
    pairs = [tuple(pair.split(',')) for pair in data]

    total = 0
    for l, r in pairs:
        la, lb = l.split('-')
        ra, rb = r.split('-')
        la, lb, ra, rb = int(la), int(lb), int(ra), int(rb)
        if (la <= ra and rb <= lb) or (ra <= la and lb <= rb):
            total += 1
    print(total)

    total2 = 0
    for l, r in pairs:
        la, lb = l.split('-')
        ra, rb = r.split('-')
        la, lb, ra, rb = int(la), int(lb), int(ra), int(rb)
        if (la <= ra <= lb) or (ra <= la <= rb):
            total2 += 1
    print(total2)
    # print(f'{part1(bags)=}')
    # print(f'{part2(groupedBags)=}')


if __name__ == '__main__':
    main()
