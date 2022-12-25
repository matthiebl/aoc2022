#!/usr/bin/env python3.10

from sys import argv
import advent as adv

KEY = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}


def main(file: str) -> None:
    print('Day 25')

    SNAFUs = adv.input_as_lines(file)

    decimal = 0
    for SNAFU in SNAFUs:
        factor = 1
        for i, c in enumerate(SNAFU[::-1]):
            decimal += factor * KEY[c]
            factor *= 5
    print(decimal)

    def get_snafu(decimal: int):
        if decimal == 0: return ''
        match (decimal % 5):
            case 0: return get_snafu(decimal // 5) + '0'
            case 1: return get_snafu(decimal // 5) + '1'
            case 2: return get_snafu(decimal // 5) + '2'
            case 3: return get_snafu(decimal // 5 + 1) + '='
            case 4: return get_snafu(decimal // 5 + 1) + '-'
    print(get_snafu(decimal))


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '25.in'
    main(file)
