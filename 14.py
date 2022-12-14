#!/usr/bin/env python3

from sys import argv
import advent as adv

DAY = 14


def getMove(x, y, cave):
    if y == len(cave) - 1:
        return None
    if cave[y + 1][x] == '.':
        return (x, y + 1)
    if cave[y + 1][x - 1] == '.':
        return (x - 1, y + 1)
    if cave[y + 1][x + 1] == '.':
        return (x + 1, y + 1)
    return None


def main(file):
    print(f'Day {DAY}')

    paths = adv.input_as_lines(file, map=lambda s: adv.double_sep(s, ' -> ', ',', map=int, group=tuple))

    maxY = 0
    for path in paths:
        for _, y in path:
            maxY = max(y, maxY)

    cave = adv.array_2D('.', 2 * maxY + 5, maxY + 2)

    for path in paths:
        x1, y1 = path.pop(0)
        while len(path) > 0:
            x2, y2 = path.pop(0)
            for x in range(x1, x2 + (1 if x1 <= x2 else -1), 1 if x1 <= x2 else -1):
                for y in range(y1, y2 + (1 if y1 <= y2 else -1), 1 if y1 <= y2 else -1):
                    cave[y][x - 500 + maxY + 2] = '#'
            x1, y1 = x2, y2

    cave[0][500 - 500 + maxY + 2] = '+'

    placed = 0
    p1 = False
    while True:
        sandx, sandy = 500 - 500 + maxY + 2, 0

        while getMove(sandx, sandy, cave) is not None:
            sandx, sandy = getMove(sandx, sandy, cave)

        if not p1 and sandy == maxY + 1:
            print(placed)
            p1 = True
        cave[sandy][sandx] = 'o'
        placed += 1
        if sandy == 0:
            break

    print(placed)


if __name__ == '__main__':
    input_file = argv[1] if len(argv) >= 2 else f'{DAY}.in'
    main(input_file)
