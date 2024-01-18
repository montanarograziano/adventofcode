# Advent of code Year 2023 Day 12 solution
# Author = montanarograziano
# Date = December 2023
import re
from functools import cache
from itertools import permutations


@cache
def find_perms(subs):
    return set(permutations(subs))


def part1():
    with open(__file__.rstrip("aoc.py") + "input.txt", "r") as input_file:
        total = 0
        input = input_file.read().splitlines()
        springs, groups = (
            [line.split(" ")[0] for line in input],
            [line.split(" ")[1] for line in input],
        )
        idx = 1
        for s, c in zip(springs, groups):
            print(idx)
            subs = []
            to_fill = sum(int(i) for i in c.split(",")) - s.count("#")
            for i in range(s.count("?")):
                if i < to_fill:
                    subs.append("#")
                else:
                    subs.append(".")

            # Generate all possible combinations of subs
            perms = find_perms(tuple(subs))
            for possible_sub in perms:
                possible_sub = list(possible_sub)
                # Substitute the current string with the list of subs
                cur = re.compile(r"\?").sub(lambda x: possible_sub.pop(0), s)
                new = re.sub(r"\.{2,}", ".", cur)
                # Check if valid configuration
                groups = re.compile(r"#+").findall(new)
                nums = c.split(",")
                if all([len(g) == int(n) for g, n in zip(groups, nums)]):
                    total += 1
            idx += 1

    return total


def part2():
    with open("input.txt", "r") as input_file:
        input = input_file.read()

    pass


print("Part One : " + str(part1()))

print("Part Two : " + str(part2()))
