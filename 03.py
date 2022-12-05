#!/usr/bin/env python3

from sys import stdin

def getItemValue(item: str) -> int:
    # Lowercase
    if item.islower():
        return ord(item) - ord('a') + 1
    # Uppercase
    return ord(item) - ord('A') + 1 + 26

def part1(bags: list) -> int:
    return sum(getItemValue(set(bag[:len(bag)//2]).intersection(set(bag[len(bag)//2:])).pop()) for bag in bags)

def part2(groupedBags: list) -> int:
    total = 0
    for group in groupedBags:
        common = set(group[0])
        for bag in group:
            common = common.intersection(set(bag))
        total += getItemValue(common.pop())
    return total

def main():
    print('Day 03')

    bags = stdin.read().split('\n')
    groupedBags = [bags[i:i+3] for i in range(0, len(bags) - 1, 3)]

    print(f'{part1(bags)=}')
    print(f'{part2(groupedBags)=}')


if __name__ == '__main__':
    main()
