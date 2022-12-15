#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def man_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def main(file: str) -> None:
    print('Day 15')
    print('Hold on... this will take a few seconds...')

    sensors = adv.input_as_lines(file, map=lambda s: adv.double_sep(s[12:], ': closest beacon is at x=', ', y=', map=int, group=tuple))

    beacon = None
    for CHECK_Y in range(4000000 + 1):
        on_check = set()
        p1 = []
        for (sx, sy), (bx, by) in sensors:
            dist = man_dist(sx, sy, bx, by)
            if by == CHECK_Y:
                on_check.add(bx)
            if not (sy - dist <= CHECK_Y <= sy + dist):
                continue
            along = dist - abs(CHECK_Y - sy)
            rx1 = sx - along
            rx2 = sx + along
            p1.append((rx1, rx2))

        p1.sort(key=lambda t: t[0])

        new_p1 = []
        x1, x2 = p1.pop(0)
        while len(p1) > 0:
            x3, x4 = p1.pop(0)
            if x2 >= x3:
                x2 = max(x2, x4)
            else:
                new_p1.append((x1, x2))
                x1, x2 = x3, x4
        new_p1.append((x1, x2))
        # print(new_p1)
        if len(new_p1) != 1:
            beacon = (new_p1[0][1] + 1, CHECK_Y)
            if CHECK_Y > (10 if file == '15.ex' else 2000000):
                break

        if (CHECK_Y == (10 if file == '15.ex' else 2000000)):
            used_places = sum(x2 - x1 + 1 for x1, x2 in new_p1)
            print(used_places - len(on_check))
            if beacon:
                break

    if beacon:
        print(beacon[0] * 4000000 + beacon[1])


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '15.in'
    main(file)
