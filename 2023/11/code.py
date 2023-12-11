# Advent of code Year 2023 Day 11 solution
# Author = ?
# Date = December 2018
from itertools import combinations


def find_dist(g1, g2, mod):
    map = {"1": 1, "2": 1000000, "#": 1}
    y, x = abs(g2[0] - g1[0]), abs(g2[1] - g1[1])
    y0 = min(g1[0], g2[0])
    x0 = min(g1[1], g2[1])
    s = 0
    for i in range(x0, x0 + x):
        s += map[mod[y0][i + 1]]
    for i in range(y0, y0 + y):
        s += map[mod[i + 1][x0]]
    return s


def part1():
    pass


def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        original = [
            [c.replace(".", "1") for c in line.strip()]
            for line in input_file.readlines()
        ]
        mod = []
        for line in original:
            if all(c == "1" for c in line):
                mod.append(["2"] * len(line))
            else:
                mod.append(line.copy())

        for i in range(len(original[0])):
            if all(line[i] == "1" for line in original):
                for line in mod:
                    line[i] = "2"

        d = {}
        galaxies = []
        idx = 1
        for i in range(len(mod)):
            for j in range(len(mod[0])):
                if mod[i][j] == "#":
                    galaxies.append((i, j, idx))
                    idx += 1
        combs = list(combinations(galaxies, 2))
        for comb in combs:
            if comb not in d and (comb[1], comb[0]) not in d:
                d[comb] = find_dist(*comb, mod)

        return sum(d.values())


print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
