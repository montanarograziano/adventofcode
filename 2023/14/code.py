# Advent of code Year 2023 Day 14 solution
# Author = montanarograziano
# Date = December 2023
import sys

FILENAME = sys.argv[1] if len(sys.argv) > 1 else "test.txt"


def cycle(grid):
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = [
            "#".join(
                [
                    "".join(sorted(tuple(group), reverse=True))
                    for group in row.split("#")
                ]
            )
            for row in grid
        ]
        grid = tuple([row[::-1] for row in grid])
    return grid


def part1():
    with open((__file__.rstrip("code.py") + FILENAME), "r") as input_file:
        grid = input_file.read().splitlines()
        grid = list(map("".join, zip(*grid)))
        grid = [
            "#".join(
                tuple(
                    "".join(sorted(list(group), reverse=True))
                    for group in row.split("#")
                )
            )
            for row in grid
        ]

        grid = list(map("".join, zip(*grid)))
        s = sum((row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))

        return s


def part2():
    with open((__file__.rstrip("code.py") + FILENAME), "r") as input_file:
        grid = tuple(input_file.read().splitlines())
        seen = {grid}
        array = [grid]

        iter = 0
        while True:
            iter += 1
            grid = cycle(grid)
            if grid in seen:
                break
            seen.add(grid)
            array.append(grid)

        first = array.index(grid)

        grid = array[(1000000000 - first) % (iter - first) + first]

        return sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid))


def main():
    print(f"Reading file {FILENAME}")
    print("Part One : " + str(part1()))
    print("Part Two : " + str(part2()))


if __name__ == "__main__":
    main()
