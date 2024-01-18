# Advent of code Year 2023 Day 17 solution
# Author = montanarograziano
# Date = December 2023
import sys
from heapq import heappop, heappush

FILENAME = sys.argv[1] if len(sys.argv) > 1 else "test.txt"





def solve_cond(part, n, dr, dc):
    if part == 1:
        return n < 3 and (dr, dc) != (0, 0)
    else:
        return 4 <= n <= 10 and (dr, dc) != (0, 0)


def dijkstra_part1(grid: list[list[int]]) -> int:
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]  # (loss, row, col, drow, dcol, num_steps)

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)

        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            return hl

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))

        if n < 3 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))


def dijkstra_part2(grid: list[list[int]]) -> int:
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]  # (loss, row, col, drow, dcol, num_steps)

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)

        if r == len(grid) - 1 and c == len(grid[0]) - 1 and n >= 4:
            return hl

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))

        if n < 10 and (dr, dc) != (0, 0):  # Can go straight
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        if n >= 4 or (dr, dc) == (0, 0):  # Can turn
            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))


def part1() -> int:
    with open((__file__.rstrip("code.py") + FILENAME), "r") as input_file:
        grid = [list(map(int, line.strip())) for line in input_file.read().splitlines()]
        return dijkstra_part1(grid)


def part2() -> int:
    with open((__file__.rstrip("code.py") + FILENAME), "r") as input_file:
        grid = [list(map(int, line.strip())) for line in input_file.read().splitlines()]
        return dijkstra_part2(grid)

def main():
    print("Part One : " + str(part1()))
    print("Part Two : " + str(part2()))


if __name__ == "__main__":
    main()