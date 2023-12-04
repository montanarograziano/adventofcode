# Advent of code Year 2023 Day 3 solution
# Author = montanarograziano
# Date = December 2023
from collections import defaultdict


def find_nums(input, nums):
    for i, line in enumerate(input):
        j = 0
        while j < len(line):
            if line[j].isdecimal():
                start = j
                num = ""
                while j < len(line) and line[j].isdecimal():
                    num += line[j]
                    j += 1
                j -= 1
                nums.append((int(num), (i, start, j)))

            j += 1


def part1():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = list(map(lambda x: x.strip(), input_file.readlines()))
        nums = []
        total = 0
        find_nums(input, nums)

        for num in nums:
            part_number = False
            for i in range(num[1][0] - 1, num[1][0] + 2):
                if i >= 0 and i < len(input):
                    for j in range(num[1][1] - 1, num[1][2] + 2):
                        if j >= 0 and j < len(input[i]):
                            if not (input[i][j].isdecimal() or input[i][j] == "."):
                                part_number = True
                                total += num[0]
                                break
                    if part_number:
                        break

        return total


def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = list(map(lambda x: x.strip(), input_file.readlines()))
        total = 0
        nums = []
        find_nums(input, nums)

        gears = defaultdict(list)
        for num in nums:
            for i in range(num[1][0] - 1, num[1][0] + 2):
                if i >= 0 and i < len(input):
                    for j in range(num[1][1] - 1, num[1][2] + 2):
                        if j >= 0 and j < len(input[i]):
                            if input[i][j] == "*":
                                gears[(i, j)].append(num[0])

        for gear in gears:
            if len(gears[gear]) == 2:
                total += gears[gear][0] * gears[gear][1]

        return total


print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
