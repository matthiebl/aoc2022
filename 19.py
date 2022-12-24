#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def can_build(recipe, ore, clay, obsidian):
    return (recipe['ore'] <= ore
            and recipe['clay'] <= clay
            and recipe['obsidian'] <= obsidian)


def build(recipe, ore, clay, obsidian):
    ore -= recipe['ore']
    clay -= recipe['clay']
    obsidian -= recipe['obsidian']
    return ore, clay, obsidian


M = {}


def simulate(blueprint, time, ore, clay, obs, geo, ore_r, clay_r, obs_r, geo_r):
    if time < 0: return 0
    if time == 0: return geo

    if (time, ore, clay, obs, geo, ore_r, clay_r, obs_r, geo_r) in M:
        return M[(time, ore, clay, obs, geo, ore_r, clay_r, obs_r, geo_r)]

    this_geo = 0
    if obs_r > 0:
        i = 0
        while not can_build(blueprint['geode'], ore + ore_r * i, clay + clay_r * i, obs + obs_r * i):
            i += 1
        res = simulate(blueprint, time - 1 - i,
                       ore - blueprint['geode']['ore'] + ore_r * (1 + i),
                       clay - blueprint['geode']['clay'] + clay_r * (1 + i),
                       obs - blueprint['geode']['obsidian'] + obs_r * (1 + i),
                       geo + geo_r * (1 + i),
                       ore_r, clay_r, obs_r, geo_r + 1)
        this_geo = max(this_geo, res)

    if clay_r > 0:
        i = 0
        while not can_build(blueprint['obsidian'], ore + ore_r * i, clay + clay_r * i, obs + obs_r * i):
            i += 1
        res = simulate(blueprint, time - 1 - i,
                       ore - blueprint['obsidian']['ore'] + ore_r * (1 + i),
                       clay - blueprint['obsidian']['clay'] + clay_r * (1 + i),
                       obs - blueprint['obsidian']['obsidian'] + obs_r * (1 + i),
                       geo + geo_r * (1 + i),
                       ore_r, clay_r, obs_r + 1, geo_r)
        this_geo = max(this_geo, res)

    i = 0
    while not can_build(blueprint['clay'], ore + ore_r * i, clay + clay_r * i, obs + obs_r * i):
        i += 1
    res = simulate(blueprint, time - 1 - i,
                   ore - blueprint['clay']['ore'] + ore_r * (1 + i),
                   clay - blueprint['clay']['clay'] + clay_r * (1 + i),
                   obs - blueprint['clay']['obsidian'] + obs_r * (1 + i),
                   geo + geo_r * (1 + i),
                   ore_r, clay_r + 1, obs_r, geo_r)
    this_geo = max(this_geo, res)

    i = 0
    while not can_build(blueprint['ore'], ore + ore_r * i, clay + clay_r * i, obs + obs_r * i):
        i += 1
    res = simulate(blueprint, time - 1 - i,
                   ore - blueprint['ore']['ore'] + ore_r * (1 + i),
                   clay - blueprint['ore']['clay'] + clay_r * (1 + i),
                   obs - blueprint['ore']['obsidian'] + obs_r * (1 + i),
                   geo + geo_r * (1 + i),
                   ore_r + 1, clay_r, obs_r, geo_r)
    this_geo = max(this_geo, res)

    # if can_build(blueprint['obsidian'], ore, clay, obs):
    #     geo = max(geo, simulate(blueprint, time - 1,
    #                             ore - blueprint['obsidian']['ore'] + ore_r,
    #                             clay - blueprint['obsidian']['clay'] + clay_r,
    #                             obs - blueprint['obsidian']['obsidian'] + obs_r,
    #                             geo + geo_r,
    #                             ore_r, clay_r, obs_r + 1, geo_r))

    # if can_build(blueprint['clay'], ore, clay, obs):
    #     geo = max(geo, simulate(blueprint, time - 1,
    #                             ore - blueprint['clay']['ore'] + ore_r,
    #                             clay - blueprint['clay']['clay'] + clay_r,
    #                             obs - blueprint['clay']['obsidian'] + obs_r,
    #                             geo + geo_r,
    #                             ore_r, clay_r + 1, obs_r, geo_r))

    # if can_build(blueprint['ore'], ore, clay, obs):
    #     geo = max(geo, simulate(blueprint, time - 1,
    #                             ore - blueprint['ore']['ore'] + ore_r,
    #                             clay - blueprint['ore']['clay'] + clay_r,
    #                             obs - blueprint['ore']['obsidian'] + obs_r,
    #                             geo + geo_r,
    #                             ore_r + 1, clay_r, obs_r, geo_r))

    # geo = max(geo, simulate(blueprint, time - 1,
    #                         ore + ore_r, clay + clay_r, obs + obs_r, geo + geo_r,
    #                         ore_r, clay_r, obs_r, geo_r))

    M[(time, ore, clay, obs, geo, ore_r, clay_r, obs_r, geo_r)] = this_geo

    return this_geo


def main(file: str) -> None:
    print('Day 19')

    def mapper(s: str):
        costs = {}
        for raw in s.split(' Each ')[1:]:
            robot, cost = raw.split(' robot costs ')
            costs[robot] = {'ore': 0, 'clay': 0, 'obsidian': 0}
            for cost in cost[:-1].split(' and '):
                amount, resource = cost.split(' ')
                costs[robot][resource] = int(amount)
        return costs

    blueprints = adv.input_as_lines(file, map=mapper)

    # p1 = 0
    # for print_num, blueprint in enumerate(blueprints, start=1):
    #     res = simulate(blueprint, 24, 0, 0, 0, 0, 1, 0, 0, 0)
    #     print(print_num, res)
    #     p1 += res * print_num
    #     M.clear()
    # print(p1)
    # print()

    p2 = 1
    for blueprint in blueprints[:3]:
        res = simulate(blueprint, 32, 0, 0, 0, 0, 1, 0, 0, 0)
        print(res)
        M.clear()
        p2 *= res
    print(p2)


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '19.in'
    main(file)
