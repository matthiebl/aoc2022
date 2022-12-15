#!/usr/bin/env python3

from sys import argv
from os import chmod
from re import findall
from aocd import get_data
from typing import Callable, Iterable, TypeVar
from ast import literal_eval

YEAR = 2022
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


def find_digits(s: str, map: Callable[[str], A] = int, group: Callable[[str], B] = list) -> 'B[A]':
    return group(map(digit) for digit in findall(r'(-[0-9]+)', s))


def groups_of(it: Iterable[A], by: int) -> list[Iterable[A]]:
    return [it[i:i + by] for i in range(0, len(it), by)]


def array_2D(base: A, width: int, height: int) -> list[list[A]]:
    return [[base] * width for _ in range(height)]


def array_3D(base: A, x: int, y: int, z: int) -> list[list[list[A]]]:
    return [array_2D(base, x, y) for _ in range(z)]


def list_eval(s: str) -> list:
    return literal_eval(s)


def create_input(day: str) -> None:
    with open(f'{day}.in', 'w') as f:
        f.write(get_data(day=int(day), year=YEAR))


def create_script(day: str) -> None:
    with open(f'{day}.py', 'w') as f:
        f.write(
            f"""#!/usr/bin/env python3.10

from sys import argv
import advent as adv

def main(file: str) -> None:
    print('Day {day}')

    data = adv.input_as_lines(file)

if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '{day}.in'
    main(file)
""")
    chmod(f'{day}.py', 0o744)


if __name__ == '__main__':
    if len(argv) != 3 or argv[1] not in ['script', 'input', 'setup'] or not argv[2].isdigit():
        print(f'Usage: \'{argv[0]} [command] <day>')
        exit(1)
    command = argv[1]
    day = argv[2]

    if command == 'script':
        create_script(day)
    elif command == 'input':
        create_input(day)
    elif command == 'setup':
        create_script(day)
        create_input(day)
