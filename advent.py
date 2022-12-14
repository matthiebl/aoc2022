#!/usr/bin/env python3

from typing import Callable, TypeVar

A = any
B = any


def read_input(file: str) -> str:
    return open(file, 'r').read()


def input_as_lines(file: str, map: Callable[[str], A] = str) -> list[A]:
    return [map(line) for line in read_input(file).split('\n')]


def input_from_grouped_lines(file: str, map: Callable[[str], A] = str) -> list[list[A]]:
    return [[map(line) for line in group.split('\n')] for group in read_input(file).split('\n\n')]


def double_sep(
    s: str,
    sep1: str,
    sep2: str,
    map: Callable[[str], A] = str,
    group: Callable[[list], B] = list
) -> list['B[A]']:
    return [group(map(b) for b in a.split(sep2)) for a in s.split(sep1)]


def array_2D(base: A, width: int, height: int) -> list[list[A]]:
    return [[base] * width for _ in range(height)]


if __name__ == '__main__':
    print('This module isn\'t supposed to be run as a program...')
    exit(1)
