#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def main(file: str) -> None:
    print('Day 21')

    data = adv.input_as_lines(file, map=lambda s: s.split(': '))
    jobs = {}
    for monkey, job in data:
        if job.isnumeric():
            jobs[monkey] = int(job)
        else:
            jobs[monkey] = tuple(job.split(' '))

    def determine(monkey: str) -> int:
        if isinstance(jobs[monkey], int):
            return jobs[monkey]

        a, op, b = jobs[monkey]
        left = determine(a)
        right = determine(b)

        result = None
        if op == '+': result = left + right
        if op == '-': result = left - right
        if op == '*': result = left * right
        if op == '/': result = left // right
        # jobs[monkey] = result

        return result

    p1 = determine('root')
    print(p1)

    # This is dirty and solved by hand foy my specific input.
    jobs['humn'] = 3916491093817
    for attempt in range(3916491093800, 3916491094000):
        jobs['humn'] = attempt

        a, _, b = jobs['root']
        left = determine(a)
        right = determine(b)

        if left == right:
            print(attempt)
            break


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '21.in'
    main(file)
