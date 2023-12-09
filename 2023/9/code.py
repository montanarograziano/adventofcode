# Advent of code Year 2023 Day 9 solution
# Author = ?
# Date = December 2018


def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = input_file.read()


def help1(s):
    if sum(i != 0 for i in s) == 0:
        return 0
    m = []
    for i in range(len(s) - 1):
        m.append(s[i + 1] - s[i])
    return s[-1] + help1(m)


def help2(s):
    if sum(i != 0 for i in s) == 0:
        return 0
    m = []
    for i in range(len(s) - 1):
        m.append(s[i + 1] - s[i])
    return s[0] - help2(m)


def part1():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        l = [
            [int(i) for i in s.split()]
            for s in input_file.read().split("\n")
            if s.strip()
        ]

    return sum(help1(i) for i in l)


def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        l = [
            [int(i) for i in s.split()]
            for s in input_file.read().split("\n")
            if s.strip()
        ]

    return sum(help2(i) for i in l)


print("Part One : " + str(part1()))

print("Part Two : " + str(part2()))
