# Advent of code Year 2023 Day 13 solution
# Author = montanarograziano
# Date = December 2023


def help(grid, part):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        if part == 1:
            above = above[: (len(below))]
            below = below[: (len(above))]
            if above == below:
                return r
        else:
            if (
                sum(
                    sum(0 if a == b else 1 for a, b in zip(x, y))
                    for x, y in zip(above, below)
                )
                == 1
            ):
                return r
    return 0


def part1():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        total = 0
        for block in input_file.read().split("\n\n"):
            grid = block.splitlines()

            row = help(grid, 1)
            total += row * 100

            cols = list(zip(*grid))
            col = help(cols, 1)
            total += col

        return total


def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        total = 0
        for block in input_file.read().split("\n\n"):
            grid = block.splitlines()

            row = help(grid, 2)
            total += row * 100

            cols = list(zip(*grid))
            col = help(cols, 2)
            total += col

        return total


print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
