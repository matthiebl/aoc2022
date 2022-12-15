#!/usr/bin/env python3.10

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

    def mapper(s): return adv.double_sep(s, ' -> ', ',', map=int, group=tuple)
    paths: list[list] = adv.input_as_lines(file, map=mapper)

    my = 0
    filled = set()
    for path in paths:
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for xx in range(x1, x2 + 1):
                for yy in range(y1, y2 + 1):
                    filled.add((xx, yy))
                    my = max(my, yy)

    into_abyss = False
    placed = 0
    while True:
        x, y = 500, 0
        if (x, y) in filled:
            break
        while True:
            if y == my + 1:
                if not into_abyss:
                    print(placed)
                    into_abyss = True
                filled.add((x, y))
                break
            if (x, y + 1) not in filled:
                y += 1
                continue
            if (x - 1, y + 1) not in filled:
                x -= 1
                y += 1
                continue
            if (x + 1, y + 1) not in filled:
                x += 1
                y += 1
                continue
            filled.add((x, y))
            break
        placed += 1
    print(placed)


if __name__ == '__main__':
    input_file = argv[1] if len(argv) >= 2 else f'{DAY}.in'
    main(input_file)
