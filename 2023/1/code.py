# Advent of code Year 2023 Day 1 solution
# Author = montanarograziano
# Date = December 2023


def part1():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = input_file.readlines()
        out = 0
        for line in input:
            curr_line = [c for c in line if c.isnumeric()]
            out += int(curr_line[0] + curr_line[-1])
        return out


def part2():
    map_char_to_value = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = input_file.readlines()
        out = 0
        curr_line = ""
        for line in input:
            curr_line = line
            for val in map_char_to_value:
                # Trick here is to replace "one" with "one1one" to avoid missing
                # nums like "twone".
                curr_line = curr_line.replace(val, val + map_char_to_value[val] + val)

            curr_line = [c for c in curr_line if c.isnumeric()]
            out += int(curr_line[0] + curr_line[-1])

        return out


print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
