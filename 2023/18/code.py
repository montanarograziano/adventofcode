# Advent of code Year 2023 Day 18 solution
# Author = ?
# Date = December 2018
import sys

FILENAME = sys.argv[1] if len(sys.argv) > 1 else "test.txt"

dir_map = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}


def parse():
    with open(FILENAME) as f:
        return f.read().splitlines()


def part1():
    grid = parse()
    seen = set()
    cur = (0, 0)
    seen |= {cur}
    for line in grid:
        d, v, c = line.split()
        dr, dc = dir_map[d]

        for _ in range(int(v)):
            cur = (cur[0] + dr, cur[1] + dc)
            # print(cur)
            seen.add(cur)
    min_col = min(seen, key=lambda x: x[1])[1]
    min_row = min(seen, key=lambda x: x[0])[0]
    print(min_col, min_row)

    width = max(seen, key=lambda x: x[1])[1] + 1
    height = max(seen, key=lambda x: x[0])[0] + 1
    print(width, height)

    s = 0
    for i in range(min_row, height):
        # for each row, sum the difference between the highest col and the lowest #col
        # find all s in seen with row i
        cur_row = sorted([c for r, c in seen if r == i])
        print(i, cur_row)
        s += abs(cur_row[-1] - cur_row[0]) + 1

    # return sum of of count of # in each row
    return s


def part2():
    grid = parse()


def main():
    print("Part One : " + str(part1()))
    print("Part Two : " + str(part2()))


if __name__ == "__main__":
    main()
