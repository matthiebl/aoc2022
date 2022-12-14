#!/usr/bin/env python3

from sys import stdin


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

    maxY = 0
    for path in paths:
        for _, y in path:
            maxY = max(y, maxY)

    cave = [['.'] * (2 * maxY + 5) for _ in range(maxY + 2)]

    for path in paths:
        x1, y1 = path.pop(0)
        while len(path) > 0:
            x2, y2 = path.pop(0)
            for x in range(x1, x2 + (1 if x1 <= x2 else -1), 1 if x1 <= x2 else -1):
                for y in range(y1, y2 + (1 if y1 <= y2 else -1), 1 if y1 <= y2 else -1):
                    cave[y][x-500+maxY+2] = '#'
            x1, y1 = x2, y2

    cave[0][500-500+maxY+2] = '+'

    placed = 0
    p1 = False
    while True:
        sandx, sandy = 500-500+maxY+2, 0

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
    main()
