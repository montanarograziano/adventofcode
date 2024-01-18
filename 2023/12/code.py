# Advent of code Year 2023 Day 12 solution
# Author = montanarograziano
# Date = December 2023
import sys

FILENAME = sys.argv[1] if len(sys.argv) > 1 else "test.txt"


def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0
    if nums == ():
        return 0 if "#" in cfg else 1

    result = 0
    if cfg[0] in ".?":
        result += count(cfg[1:], nums)

    if cfg[0] in "#?":
        if (
            nums[0] <= len(cfg)
            and "." not in cfg[: nums[0]]
            and (nums[0] == len(cfg) or cfg[nums[0]] != "#")
        ):
            result += count(cfg[nums[0] + 1 :], nums[1:])

    return result


def part1():
    with open(__file__.rstrip("code.py") + FILENAME, "r") as input_file:
        input = input_file.read().splitlines()
        total = 0
        for line in input:
            cfg, nums = line.split()
            nums = tuple(map(int, nums.split(",")))
            total += count(cfg, nums)

    return total


def part2():
    with open(__file__.rstrip("code.py") + FILENAME, "r") as input_file:
        input = input_file.read().splitlines()

    pass


def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
