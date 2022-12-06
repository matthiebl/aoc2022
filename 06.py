#!/usr/bin/env python3

from sys import stdin
import re

def part1(datastream: str) -> int:
    targetLen = 4
    for i in range(targetLen, len(datastream)):
        if len(set(datastream[i-targetLen:i])) == targetLen:
            return i

def part2(datastream: str) -> int:
    targetLen = 14
    for i in range(targetLen, len(datastream)):
        if len(set(datastream[i-targetLen:i])) == targetLen:
            return i

def main():
    print('Day 06')

    datastream = stdin.read()

    print(f'{part1(datastream)=}')
    print(f'{part2(datastream)=}')
    

if __name__ == '__main__':
    main()
