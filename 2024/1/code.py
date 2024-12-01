# Advent of code Year 2024 Day 1 solution
# Author = montanarograziano
# Date = December 2024


def part1():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = input_file.read().splitlines()
        lines = [line.split() for line in input]
        left, right = [list(x) for x in zip(*lines)]
        left.sort()
        right.sort()
        result = 0
        for i in range(len(left)):
            result += abs(int(left[i]) - int(right[i]))

        return result


def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = input_file.read().splitlines()
        lines = [line.split() for line in input]
        left, right = [list(x) for x in zip(*lines)]
        result = 0
        d = {x: 0 for x in left}
        for num in right:
            if num in d:
                d[num] += 1

        for k, v in d.items():
            result += int(k) * v

        return result


print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
