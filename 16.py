#!/usr/bin/env python3.10

from sys import argv
from re import split
import advent as adv


def main(file: str) -> None:
    print('Day 16')

    def mapper(s): return (s[6:8], *split(r'; tunnels? leads? to valves? ', s[23:]))
    data = [(a, int(b), c.split(', ')) for a, b, c in adv.input_as_lines(file, map=mapper)]

    F = {valve: val for valve, val, _ in data}
    G = {valve: leads for valve, _, leads in data}

    def bfs(S, t, O):
        R = []
        V = set()
        queue = [(S, t)]
        while len(queue) > 0:
            v, t = queue.pop(0)
            if v in V or t == 0: continue

            V.add(v)
            vtf = (v, t - 1, (t - 1) * F[v])
            if v not in O and vtf[-1] > 0:
                R.append(vtf)

            for valve in G[v]:
                queue.append((valve, t - 1))
        return R

    def simulate(s: str, t: int, O: set):
        if t <= 0: return 0

        best = 0
        for valve, t, flow in bfs(s, t, O):
            O_ = O.copy()
            O_.add(valve)
            best = max(flow + simulate(valve, t, O_), best)
        return best

    def simulate_help(s1: str, t1: int, s2: str, t2: int, O: set):
        if t1 <= 0 and t2 <= 0: return 0
        if t1 <= 0: return simulate(s2, t2, O)
        if t2 <= 0: return simulate(s1, t1, O)

        best = 0
        options1 = bfs(s1, t1, O)
        if sum(op[-1] for op in options1) <= best:
            return best
        for v1, tt1, f1 in options1:
            # print(f'{v1=} {tt1=} {f1=}')
            O_ = O.copy()
            O_.add(v1)
            # print(O_, s2, t2, bfs(s2, t2, O_))
            # best = max(f1 + simulate_help(v1, t1, s2, t2, O_), best)

            options2 = bfs(s2, t2, O_)
            if f1 + sum(op[-1] for op in options2) <= best:
                return best
            for v2, tt2, f2 in bfs(s2, t2, O_):
                # print(f'    {v2=} {tt2=} {f2=}')
                O__ = O_.copy()
                O__.add(v2)
                best = max(f1 + f2 + simulate_help(v1, tt1, v2, tt2, O__), best)
        return best

    print(simulate('AA', 30, set()))
    print(simulate_help('AA', 26, 'AA', 26, set()))


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '16.in'
    main(file)
