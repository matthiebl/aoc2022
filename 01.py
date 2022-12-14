#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def main(file: str) -> None:
    print('Day 01')

    elves = adv.input_from_grouped_lines(file, map=int)

    p1 = max(sum(elf) for elf in elves)
    print(p1)

    p2 = sum(sorted(sum(elf) for elf in elves)[-3:])
    print(p2)


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '01.in'
    main(file)
