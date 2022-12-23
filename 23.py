#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def main(file: str) -> None:
    print('Day 23')

    data = adv.input_as_lines(file)

    elves = set()
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == '#': elves.add((x, y))

    search_queue = ['N', 'S', 'W', 'E']

    def round(elves: set, search: list) -> int:
        happy = 0
        proposed = {}
        moves = {}
        for (x, y) in elves:
            if sum((x + dx, y + dy) in elves for dy in [-1, 0, 1] for dx in [-1, 0, 1]) == 1:
                moves[(x, y)] = (x, y)
                happy += 1
                continue

            for direction in search:
                if direction == 'N' and sum((x + dx, y - 1) in elves for dx in [-1, 0, 1]) == 0:
                    proposed[(x, y - 1)] = proposed.get((x, y - 1), 0) + 1
                    moves[(x, y)] = (x, y - 1)
                    break
                if direction == 'S' and sum((x + dx, y + 1) in elves for dx in [-1, 0, 1]) == 0:
                    proposed[(x, y + 1)] = proposed.get((x, y + 1), 0) + 1
                    moves[(x, y)] = (x, y + 1)
                    break
                if direction == 'E' and sum((x + 1, y + dy) in elves for dy in [-1, 0, 1]) == 0:
                    proposed[(x + 1, y)] = proposed.get((x + 1, y), 0) + 1
                    moves[(x, y)] = (x + 1, y)
                    break
                if direction == 'W' and sum((x - 1, y + dy) in elves for dy in [-1, 0, 1]) == 0:
                    proposed[(x - 1, y)] = proposed.get((x - 1, y), 0) + 1
                    moves[(x, y)] = (x - 1, y)
                    break
                moves[(x, y)] = (x, y)

        first = search.pop(0)
        search.append(first)

        elves.clear()
        for curr, new in moves.items():
            if curr == new or proposed[new] > 1:
                elves.add(curr)
            else:
                elves.add(new)

        return happy

    for _ in range(10):
        round(elves, search_queue)

        # map = adv.array_2D('.', 14, 12)
        # for x, y in elves:
        #     map[y][x] = '#'
        # for y in map:
        #     print(''.join(y))
        # print()

    p1 = 0
    x1, y1, x2, y2 = adv.min_max_x_y(elves)
    for xx in range(x1, x2 + 1):
        for yy in range(y1, y2 + 1):
            if (xx, yy) not in elves:
                p1 += 1
    print(p1)

    rounds = 10

    while round(elves, search_queue) != len(elves):
        rounds += 1

    print(rounds + 1)


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '23.in'
    main(file)
