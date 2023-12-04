# Advent of code Year 2023 Day 4 solution
# Author = montanarograziano
# Date = December 2023
import re


def part1():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = list(map(lambda x: x.split(":")[1].strip(), input_file.readlines()))
        points = 0
        for line in input:
            winning_cards, my_cards = line.split("|")
            win_nums = set(re.findall(r"\d+", winning_cards))
            my_nums = set(re.findall(r"\d+", my_cards))
            inters = win_nums.intersection(my_nums)
            points += 2 ** (len(inters) - 1) if len(inters) > 0 else 0

        return points


def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = list(map(lambda x: x.split(":")[1].strip(), input_file.readlines()))
        card_dict = {i: 1 for i in range(1, len(input) + 1)}
        for i, line in enumerate(input):
            winning_cards, my_cards = line.split("|")
            win_nums = set(re.findall(r"\d+", winning_cards))
            my_nums = set(re.findall(r"\d+", my_cards))
            inters = win_nums.intersection(my_nums)
            if inters:
                for j in range(i + 2, i + len(inters) + 2):
                    card_dict[j] += 1 * card_dict[i + 1]

    return sum(card_dict.values())


print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
