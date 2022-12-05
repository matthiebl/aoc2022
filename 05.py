#!/usr/bin/env python3

from sys import stdin
import re

def part1(stacks: list[list], moves: list[tuple]) -> str:
    for move in moves:
        amount, source, dest = move
        for _ in range(amount):
            box = stacks[source-1].pop(0)
            stacks[dest-1].insert(0, box)
    return ''.join(stack[0] for stack in stacks)

def part2(stacks: list[list], moves: list[tuple]) -> int:
    for move in moves:
        amount, source, dest = move
        boxes = stacks[source-1][:amount]
        stacks[source-1] = stacks[source-1][amount:]

        boxes.extend(stacks[dest-1])
        stacks[dest-1] = boxes
    return ''.join(stack[0] for stack in stacks)

def main():
    print('Day 04')

    stackData, moves = stdin.read().split('\n\n')
    stackData = stackData.split('\n')

    stacks = [list() for i in range(len(stackData[0]) // 4)]
    for line in stackData[:-1]:
        for i in range(1, len(line), 4):
            if line[i] != ' ': stacks[i//4].append(line[i])
    moves = [tuple(map(int, re.split(r'move | from | to ', move)[1:])) for move in moves.split('\n')]

    copy = [stack.copy() for stack in stacks]
    print(part1(copy, moves))
    print(part2(stacks, moves))

if __name__ == '__main__':
    main()
