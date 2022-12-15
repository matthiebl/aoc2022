#!/usr/bin/env python3.10

from sys import argv
import advent as adv

TUNING_FREQ = 4000000


def man_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def main(file: str) -> None:
    print('Day 15')
    print('Hold on... this may take a few seconds...')

    Y_RANGE = 20 if file == '15.ex' else 4000000
    Y_CHECK = 10 if file == '15.ex' else 2000000

    def mapper(s): return adv.double_sep(s[12:], ': closest beacon is at x=', ', y=', map=int, group=tuple)
    sensors = adv.input_as_lines(file, map=mapper)

    missing_beacon = None
    for Y in range(Y_RANGE + 1):
        beacons = set()
        invalid_ranges = []

        # Find all the ranges along y = Y where a sensor can reach
        for (sx, sy), (bx, by) in sensors:
            dist = man_dist(sx, sy, bx, by)
            if not (sy - dist <= Y <= sy + dist):
                continue
            if by == Y: beacons.add(bx)

            dist_on_Y = dist - abs(Y - sy)
            rx1 = sx - dist_on_Y
            rx2 = sx + dist_on_Y

            invalid_ranges.append((rx1, rx2))

        invalid_ranges.sort(key=lambda t: t[0])

        # Sort the ranges
        temp_ranges = []
        x1, x2 = invalid_ranges.pop(0)
        while len(invalid_ranges) > 0:
            x3, x4 = invalid_ranges.pop(0)
            if x2 >= x3:
                x2 = max(x2, x4)
            else:
                temp_ranges.append((x1, x2))
                x1, x2 = x3, x4
        temp_ranges.append((x1, x2))
        invalid_ranges = temp_ranges

        # If we find a gap in the ranges, thats the missing beacon
        if len(invalid_ranges) != 1:
            missing_beacon = (invalid_ranges[0][1] + 1, Y)
            if Y > Y_CHECK: break

        # If we reach the check level, count how
        # many places cannot be the missing beacon
        if Y == Y_CHECK:
            p1 = sum(x2 - x1 + 1 for x1, x2 in invalid_ranges) - len(beacons)
            print(p1)
            if missing_beacon: break

    p2 = missing_beacon[0] * TUNING_FREQ + missing_beacon[1]
    print(p2)


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '15.in'
    main(file)
