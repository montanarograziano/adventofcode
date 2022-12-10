# Advent of code Year 2022 Day 6 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()


def part1(line, size):
    for i, _ in enumerate(line):
        current_substring = line[i:i+size]
        packet = set(current_substring)
        if len(packet) == size:
            return i + size
    return -1


print("Part One : " + str(part1(input, 4)))

print("Part Two : " + str(part1(input, 14)))
print(input[3546:3560])
