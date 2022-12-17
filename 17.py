#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def main(file: str) -> None:
    print('Day 17')

    current = adv.read_input(file)
    blocks = [
        [(2, 0), (3, 0), (4, 0), (5, 0)],
        [(3, 2), (2, 1), (3, 1), (4, 1), (3, 0)],
        [(4, 2), (4, 1), (2, 0), (3, 0), (4, 0)],
        [(2, 3), (2, 2), (2, 1), (2, 0)],
        [(2, 1), (3, 1), (2, 0), (3, 0)],
    ]

    placed = set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
    top = 0

    airi = 0
    blocki = 0

    for round in range(1_000_000_000_000):
        if round == 2022:
            print(f'p1={top}')
        if round % 1_000_000 == 0:
            print(round)
        block = [(x, y + top + 4) for x, y in blocks[blocki % len(blocks)]]
        blocki += 1

        while True:
            air = current[airi % len(current)]
            airi += 1

            if air == '>' and all([x < 6 and (x + 1, y) not in placed for x, y in block]):
                block = [(x + 1, y) for x, y in block]
            if air == '<' and all([x > 0 and (x - 1, y) not in placed for x, y in block]):
                block = [(x - 1, y) for x, y in block]

            if any([(x, y - 1) in placed for x, y in block]):
                for x, y in block:
                    top = max(top, y)
                    placed.add((x, y))
                break
            block = [(x, y - 1) for x, y in block]
    print(top)


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '17.in'
    main(file)
