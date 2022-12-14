#!/usr/bin/env python3

from sys import stdin


def showCave(cave: list[list[str]]) -> None:
    for row in cave:
        print(''.join(row).replace('.', '.'))


def getMove(x, y, cave):
    if y == len(cave) - 1:
        return None
    if cave[y+1][x] == '.':
        return (x, y+1)
    if cave[y+1][x-1] == '.':
        return (x-1, y+1)
    if cave[y+1][x+1] == '.':
        return (x+1, y+1)
    return None


def main():
    print('Day 14')

    paths = [[(int(coord.split(',')[0]), int(coord.split(',')[1]))
              for coord in path.split(' -> ')] for path in stdin.read().split('\n')]

    minX, minY = 500, 0
    maxX, maxY = 500, 0
    for path in paths:
        for x, y in path:
            minX = min(x, minX)
            maxX = max(x, maxX)
            minY = min(y, minY)
            maxY = max(y, maxY)

    cave = [['.'] * (maxX + 2 - (minX - 2)) for _ in range(maxY + 2)]

    for path in paths:
        x1, y1 = path.pop(0)
        while len(path) > 0:
            x2, y2 = path.pop(0)
            for x in range(x1, x2 + (1 if x1 <= x2 else -1), 1 if x1 <= x2 else -1):
                for y in range(y1, y2 + (1 if y1 <= y2 else -1), 1 if y1 <= y2 else -1):
                    cave[y][x - (minX - 2)] = '#'

            x1, y1 = x2, y2

    cave[0][500 - (minX - 2)] = '+'

    p1 = 0
    while True:
        sandx, sandy = 500 - (minX - 2), 0

        while getMove(sandx, sandy, cave) is not None:
            sandx, sandy = getMove(sandx, sandy, cave)

        if sandy == maxY + 1:
            break
        cave[sandy][sandx] = 'o'
        p1 += 1

    showCave(cave)
    print(p1)


if __name__ == '__main__':
    main()
