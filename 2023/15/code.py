# Advent of code Year 2023 Day 15 solution
# Author = montanarograziano
# Date = December 2023

from typing import Dict


def _hash(s):
    i = 0
    for c in s:
        i = (i + ord(c)) * 17 % 256
    return i


def part1():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = input_file.read().strip()
        tot = sum([_hash(s) for s in input.split(",")])

        return tot


def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = input_file.read().strip()
        tot = 0
        boxes: Dict[int, Dict[str, int]] = {i: {} for i in range(256)}
        for s in input.split(","):
            if "=" in s:
                l, f = s.split("=")
                boxes[_hash(l)][l] = int(f)
            elif "-" in s:
                l = s.split("-")[0]
                if l in boxes[_hash(l)]:
                    del boxes[_hash(l)][l]
        tot = sum(
            sum((m + 1) * v * (i + 1) for i, v in enumerate(box.values()))
            for m, box in enumerate(boxes.values())
        )

        return tot


print("Part One : " + str(part1()))
print("Part Two : " + str(part2()))
