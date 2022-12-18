#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def main(file: str) -> None:
    print('Day 18')

    points = set(adv.input_as_lines(file, map=lambda s: tuple(map(int, s.split(',')))))

    M = 1 + max(max(x for x, _, _ in points),
                max(y for _, y, _ in points),
                max(z for _, _, z in points))

    P = adv.array_3D('.', M, M, M)

    p1 = 0
    DX = [-1, 1, 0, 0, 0, 0]
    DY = [0, 0, -1, 1, 0, 0]
    DZ = [0, 0, 0, 0, -1, 1]
    for x, y, z in points:
        P[z][y][x] = '#'
        SA = 6
        for dx, dy, dz in zip(DX, DY, DZ):
            if (x + dx, y + dy, z + dz) in points:
                SA -= 1
        p1 += SA
    print(p1)

    for z in P:
        for y in z:
            print(''.join(y))
        print()


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '18.in'
    main(file)
