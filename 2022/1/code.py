# Advent of code Year 2022 Day 1 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()

calories_per_elf = input.split("\n\n")
calories_per_elf = [x.split('\n') for x in calories_per_elf]
calories_per_elf = [list(map(int, x)) for x in calories_per_elf]
calories_per_elf = [sum(x) for x in calories_per_elf]
calories_per_elf.sort(reverse=True)
total_three = sum(calories_per_elf[:3])
print("Part One : " + str(max(calories_per_elf)))

print("Part Two : " + str(total_three))
