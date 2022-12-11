#!/usr/bin/env python3

from sys import stdin
import re


def main():
    print('Day 07')

    terminal = [query.split('\n')[:-1]
                for query in stdin.read().split('$ ')][1:]
    cwd = []
    system = {}
    for result in terminal:
        cmd = result.pop(0)
        if cmd.startswith('cd'):
            path = cmd.split(' ')[1]
            if path == '/':
                cwd = ['~']
            elif path == '..':
                cwd.pop()
            else:
                cwd.append(path)
            continue

        pwd = '/'.join(cwd)
        cd = []
        for file in result:
            a, b = file.split(' ')
            if a == 'dir':
                this = ('d', f'{pwd}/{b}')
                cd.append(this)
            else:
                cd.append(('f', int(a)))
        system[pwd] = cd

    sizes = {}

    def size(d):
        if d in sizes:
            return sizes[d]

        total = 0
        for typ, data in system[d]:
            if typ == 'f':
                total += data
            else:
                total += size(data)
        sizes[d] = total
        return total

    size('~')

    free = 70_000_000 - sizes['~']
    needed = 30_000_000 - free

    total = 0
    possible = []
    for dsize in sizes.values():
        if dsize <= 100000:
            total += dsize
        if dsize >= needed:
            possible.append(dsize)
    print(total)
    print(min(possible))


if __name__ == '__main__':
    main()
