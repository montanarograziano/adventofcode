# Advent of code Year 2023 Day 2 solution
# Author = montanarograziano
# Date = December 2023


def part1():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        lines = input_file.readlines()
        sum_id = 0
        valid_game = {"red": 12, "green": 13, "blue": 14}
        for i, line in enumerate(lines):
            is_valid = True
            for subgame in line.split(": ")[1].split(";"):
                for cubes in subgame.split(","):
                    value, color = cubes.strip().split(" ")[:2]
                    if int(value) > valid_game[color]:
                        is_valid = False
            if is_valid:
                sum_id += i + 1

    return sum_id


def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        lines = input_file.readlines()
        power_cubes = 0
        for i, line in enumerate(lines):
            lowest_cubes = {"red": 0, "green": 0, "blue": 0}
            for subgame in line.split(": ")[1].split(";"):
                for cubes in subgame.split(","):
                    value, color = cubes.strip().split(" ")[:2]
                    lowest_cubes[color] = max(lowest_cubes[color], int(value))

            power_cubes += (
                lowest_cubes["red"] * lowest_cubes["green"] * lowest_cubes["blue"]
            )

    return power_cubes  


print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
