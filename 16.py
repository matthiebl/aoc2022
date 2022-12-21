#!/usr/bin/env python3.10

from sys import argv
from re import split
import advent as adv    # Personal helper functions


# Maybe more DP would help this, but it only seems to slow it down...
# or python dicts and frozenset hashing doesn't like me...
def main(file: str) -> None:
    print('Day 16')
    print('May take around 1-2 min...')

    # Parse input
    def mapper(s): return (s[6:8], *split(r'; tunnels? leads? to valves? ', s[23:]))
    data = [(a, int(b), c.split(', ')) for a, b, c in adv.input_as_lines(file, map=mapper)]

    # Graph data
    flow = {valve: val for valve, val, _ in data}
    adjacency_list = {valve: leads for valve, _, leads in data}

    # Keep track of movable options from valve with remaining time
    saved_options: dict[tuple[str, int], list] = {}

    # Find all the possible options to move to from a
    # starting position with a remaining time left
    # (excludes flow = 0 valves)
    def possible_options(start: str, time: int):
        if (start, time) in saved_options:
            return saved_options[(start, time)]

        # each (V)alve, the (T)ime if we move straight
        # there and the total (F)low from opening it
        VTF: list[tuple[str, int, int]] = []

        # Using BFS we get best path to all valves
        V = set()
        queue = [(start, time)]
        while len(queue) > 0:
            v, tt = queue.pop(0)
            if v in V or tt == 0: continue

            V.add(v)
            vtf = (v, tt - 1, (tt - 1) * flow[v])
            if vtf[-1] > 0:
                VTF.append(vtf)

            for valve in adjacency_list[v]:
                queue.append((valve, tt - 1))

        saved_options[(start, time)] = VTF
        return VTF

    # From a starting point (s), with (t) time remaining,
    # having already opened valves in (O),
    # what is the best total flow we could achieve?
    def simulate(s: str, t: int, O: set):
        if t <= 0: return 0

        best = 0
        # By moving to each valve and then trying all options from
        # that valve, find the best option
        for valve, t, flow in possible_options(s, t):
            if valve in O: continue
            O_ = O.copy()
            O_.add(valve)
            best = max(flow + simulate(valve, t, O_), best)
        return best

    # If I start from (s1) with (t1) time left, and the elephant
    # starts at (s2) with (t2) time left, having already opened
    # all (O) valves, what is the best total flow we can both
    # achieve?
    def simulate_help(s1: str, t1: int, s2: str, t2: int, O: set):
        if t1 <= 0 or t2 <= 0: return 0

        best = 0
        # For each possible valve from start, try opening that valve
        for v1, tt1, f1 in possible_options(s1, t1):
            if v1 in O: continue
            O_ = O.copy()
            O_.add(v1)

            # Quickly check if just doing the rest myself is any good
            best = max(best, f1 + simulate(v1, tt1, O_.copy()))

            # Then let the elephant try each of the options from them
            for v2, tt2, f2 in possible_options(s2, t2):
                if v2 in O_: continue
                O__ = O_.copy()
                O__.add(v2)
                best = max(f1 + f2 + simulate_help(v1, tt1, v2, tt2, O__), best)

        # This should cover the entire search space, as we
        # try all our options, the elephant tries all their options
        # and then we try every option within that recursively.
        return best

    print(simulate('AA', 30, set()))
    print(simulate_help('AA', 26, 'AA', 26, set()))


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '16.in'
    main(file)
