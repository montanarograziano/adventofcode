# Advent of code Year 2023 Day 8 solution
# Author = ?
# Date = December 2018
import math
import re


def help2(start, c, d):
    if c == "L":
        return d[start][0]
    else:
        return d[start][1]


def part1():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        d = {}
        input = input_file.readlines()
        commands = input[0].strip()
        seq = input[2:]
        # Each line in seq has the following structure AAA = (BBB, CCC)
        # Map what's left of = as a key and the right tuple as a value in d
        for line in seq:
            key, l, r = re.findall(r"(\w+)", line)
            d[key] = (l, r)

        steps = 0
        idx = 0
        current = "AAA"
        while current != "ZZZ":
            c = commands[idx % len(commands)]
            if c == "L":
                current = d[current][0]
            else:
                current = d[current][1]
            steps += 1
            idx += 1

            if current == "ZZZ":
                break
    return steps


def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        d = {}
        input = input_file.readlines()
        commands = input[0].strip()
        seq = input[2:]
        startings = []
        for line in seq:
            key, l, r = re.findall(r"(\w+)", line)
            if key.endswith("A"):
                startings.append(key)
            d[key] = (l, r)

        steps = 0
        idx = 0

        # cycle as long as every node in startings ends with Z
        lcm = []
        for s in startings:
            steps = 0
            idx = 0
            while not s.endswith("Z"):
                c = commands[idx % len(commands)]
                steps += 1
                idx += 1
                s = help2(s, c, d)
            lcm.append(steps)

        return math.lcm(*lcm)


print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
