# Advent of code Year 2023 Day 5 solution
# Author = montanarograziano
# Date = December 2023
import re


def part1():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        seeds = re.findall(r"(\d+)", input_file.readline())
        mappings = []

        text = input_file.read()
        for i, element in enumerate(text.split('\n\n')):
            element = element.strip()
            triples = element.split('\n')[1:]
            






def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = input_file.read()


print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
