#!/usr/bin/env python3

from sys import stdin

WIN = 6
DRAW = 3
LOSE = 0

ROCK, X = 'A', 1
PAPER, Y = 'B', 2
SCISSORS, Z = 'C', 3

results1 = {
    (ROCK, 'X'): DRAW + X,
    (ROCK, 'Y'): WIN + Y,
    (ROCK, 'Z'): LOSE + Z,
    (PAPER, 'X'): LOSE + X,
    (PAPER, 'Y'): DRAW + Y,
    (PAPER, 'Z'): WIN + Z,
    (SCISSORS, 'X'): WIN + X,
    (SCISSORS, 'Y'): LOSE + Y,
    (SCISSORS, 'Z'): DRAW + Z,
}

results2 = {
    (ROCK, 'X'): LOSE + Z,
    (ROCK, 'Y'): DRAW + X,
    (ROCK, 'Z'): WIN + Y,
    (PAPER, 'X'): LOSE + X,
    (PAPER, 'Y'): DRAW + Y,
    (PAPER, 'Z'): WIN + Z,
    (SCISSORS, 'X'): LOSE + Y,
    (SCISSORS, 'Y'): DRAW + Z,
    (SCISSORS, 'Z'): WIN + X,
}


def part1(plays: list) -> int:
    return sum(results1[play] for play in plays)


def part2(plays: list) -> int:
    return sum(results2[play] for play in plays)


def main():
    print('Day 02')

    plays = [(line[0], line[2]) for line in stdin.read().split('\n')]

    print(f'{part1(plays)=}')
    print(f'{part2(plays)=}')


if __name__ == '__main__':
    main()
