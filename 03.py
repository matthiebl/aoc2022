#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def item_value(item: str) -> int:
    # Lowercase
    if item.islower():
        return ord(item) - ord('a') + 1
    # Uppercase
    return ord(item) - ord('A') + 1 + 26


def main(file: str) -> None:
    print('Day 03')

    bags = adv.input_as_lines(file)
    grouped_bags = adv.groups_of(bags, 3)

    p1 = sum(item_value(set(bag[:len(bag) // 2]).intersection(set(bag[len(bag) // 2:])).pop())
             for bag in bags)
    print(p1)

    p2 = sum(item_value(set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop())
             for group in grouped_bags)
    print(p2)


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '03.in'
    main(file)
