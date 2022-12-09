# Advent of code Year 2022 Day 3 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.read().split('\n')


def prio(item):
    if "a" <= item <= "z":
        return ord(item) - ord("a") + 1
    if "A" <= item <= "Z":
        return ord(item) - ord("A") + 27
    raise RuntimeError(f"not ok: {item}")


def part1(lines):
    total = 0
    for line in lines:
        line = line.strip()
        for item in set(line[: len(line) // 2]).intersection(line[len(line) // 2:]):
            total += prio(item)
    return total


def part2(lines):
    total = 0
    for first, second, third in zip(*(map(str.strip, lines),) * 3):
        total += prio(set(first).intersection(second).intersection(third).pop())
    return total


sum_priorities = 0
sum_groups = 0
groups = []

print("Part One : " + str(part1(input)))

print("Part Two : " + str(part2(input)))
