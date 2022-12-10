#!/usr/bin/env python3

from sys import stdin


def main():
    print('Day 10')

    raw = stdin.read().split('\n')

    instructions: list[str] = []
    for ins in raw:
        if ins != 'noop':
            instructions.append('noop')
        instructions.append(ins)

    X = 1

    p1 = 0
    p2 = []
    R = ''
    for cycle, instruction in enumerate(instructions, start=1):
        if len(R) == 40:
            p2.append(R)
            R = ''
        currentPixel = len(R)  # 0
        R += '#' if X-1 <= currentPixel <= X+1 else ' '

        if (cycle - 20) % 40 == 0:
            p1 += cycle * X
        if instruction.startswith('addx'):
            X += int(instruction[5:])
    p2.append(R)

    print(p1)
    print('\n'.join(p2))


if __name__ == '__main__':
    main()
