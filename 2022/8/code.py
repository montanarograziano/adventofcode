# Advent of code Year 2022 Day 8 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()

test = '''24200
10610
24500'''


def distance(trees, curr_tree):
    i = 0
    for t in trees:
        i += 1
        if curr_tree <= t:
            return i
    return i


def part1(input):
    map = [line for line in input.split('\n')]
    max_x = len(map)
    max_y = len(map[0])
    total = 2 * (max_x + max_y) - 4
    max_score = []
    for i in range(max_x):
        for j in range(max_y):
            if 0 < i < max_x - 1 and 0 < j < max_y - 1:
                curr_tree = map[i][j]
                top = [row[j] for row in map[:i]]
                left = [x for x in map[i][:j]]
                right = [x for x in map[i][j + 1:]]
                bottom = [row[j] for row in map[i + 1:]]
                if all(curr_tree > x for x in top) or all(curr_tree > y for y in left) or all(
                        curr_tree > y for y in right) or all(curr_tree > y for y in bottom):
                    total += 1
                scenic_score = 1
                scenic_score *= distance(top[::-1], curr_tree)
                scenic_score *= distance(left[::-1], curr_tree)
                scenic_score *= distance(right, curr_tree)
                scenic_score *= distance(bottom, curr_tree)
                max_score.append(scenic_score)

    return total, max(max_score)


print("Part One : " + str(part1(input)[0]))

print("Part Two : " + str(part1(input)[1]))
