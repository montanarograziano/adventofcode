# Advent of code Year 2022 Day 5 solution
# Author = ?
# Date = December 2022
import re
from itertools import zip_longest

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()


def part1(reverse, input):
    lines = input.split('\n')
    middle = lines.index('')
    instructions = lines[middle + 1:]
    crates = lines[:middle - 1]
    initial_stacks = {}
    horizontal_rows = [re.findall(r'.{1,4}', row) for row in crates]
    for row in horizontal_rows:
        for i, r in enumerate(row):
            r = r.strip()
            if r != '':
                if i + 1 in initial_stacks:
                    initial_stacks[i + 1].append(r)
                else:
                    initial_stacks[i + 1] = [r]
    for instruction in instructions:
        qty, start, end = (re.match(r'move (\d+) from (\d+) to (\d+)', instruction).groups())
        qty, start, end = int(qty), int(start), int(end)
        temp = initial_stacks[start][:qty]
        for x in temp:
            initial_stacks[start].remove(x)
        if reverse:
            initial_stacks[end] = temp[::-1] + initial_stacks[end]
        else:
            initial_stacks[end] = temp + initial_stacks[end]

    final = ""
    for i in range(1, 10):
        final += initial_stacks[i][0] if initial_stacks[i] != [] else ""
    return final.replace("[", "").replace("]", "")


print("Part One : " + str(part1(True, input)))

print("Part Two : " + str(part1(False, input)))
