#!/usr/bin/env python3

from sys import stdin
import re

def part1(bags: list) -> int:
    return None

def part2(groupedBags: list) -> int:
    return None

def main():
    print('Day 04')

    stackData, moves = stdin.read().split('\n\n')
    stackData = stackData.split('\n')

    stacks = [list() for i in range(len(stackData[0]) // 4)]
    for line in stackData[:-1]:
        for i in range(0, len(line) - 1, 4):
            if line[i+1] != ' ': stacks[i//4].append(line[i+1])
    
    moves = [re.split(r'move | from | to ', move)[1:] for move in moves.split('\n')]

    stacks1 = [stack.copy() for stack in stacks]
    for move in moves:
        amount, f, t = move
        for _ in range(int(amount)):
            box = stacks1[int(f)-1].pop(0)
            stacks1[int(t)-1].insert(0, box)
    print(''.join([stack[0] for stack in stacks1]))

    for move in moves:
        amount, f, t = move
        boxes = stacks[int(f)-1][0:int(amount)]
        stacks[int(f)-1] = stacks[int(f)-1][int(amount):]

        boxes.extend(stacks[int(t)-1])
        stacks[int(t)-1] = boxes
    print(''.join([stack[0] for stack in stacks]))

    # print(f'{part1(bags)=}')
    # print(f'{part2(groupedBags)=}')


if __name__ == '__main__':
    main()
