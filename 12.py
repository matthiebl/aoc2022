#!/usr/bin/env python3

from sys import stdin


def main():
    print('Day 12')
    print('Part 2 may take a couple seconds...\n')

    height_map = stdin.read().split('\n')

    ROWS = len(height_map)
    COLS = len(height_map[0])

    H = list('SabcdefghijklmnopqrstuvwxyzE')
    S = None
    for r, row in enumerate(height_map):
        try:
            s = row.index('S')
            S = (r, s)
        except:
            pass

    def dfs(S):
        V = set()
        queue = [[S]]
        while len(queue) > 0:
            path = queue.pop(0)
            r, c = path[-1]
            h = H.index(height_map[r][c])
            V.add((r, c))

            if H[h] == 'E':
                return len(path)-1

            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if (0 <= r + dr < ROWS
                    and 0 <= c + dc < COLS
                    and (r+dr, c+dc) not in V
                        and height_map[r+dr][c+dc] in H[:h+2]):
                    queue.append([coord for coord in path] + [(r+dr, c+dc)])
                    V.add((r+dr, c+dc))
    p1 = dfs(S)
    print(f'{p1=}')

    dists = [p1]
    for r, row in enumerate(height_map):
        for c, col in enumerate(row):
            if col == 'a':
                dist = dfs((r, c))
                if dist:
                    dists.append(dist)
    dists.sort()
    p2 = dists[0]
    print(f'{p2=}')


if __name__ == '__main__':
    main()
