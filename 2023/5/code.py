# Advent of code Year 2023 Day 5 solution
# Author = montanarograziano
# Date = December 2023
import re


def part1():
    input_data = open(__file__.rstrip("code.py") + "input.txt").read().splitlines()
    maps = []
    for line in input_data[2:]:
        if "map" in line:
            maps.append(dict())
        elif line != "":
            destination, source, length = [int(value) for value in line.split()]
            maps[-1][range(source, source + length)] = range(
                destination, destination + length
            )

    def lookup_location(initial_value: int) -> int:
        value = initial_value
        for current_map in maps:
            value = next(
                (
                    destination_range.start + (value - source_range.start)
                    for source_range, destination_range in current_map.items()
                    if value in source_range
                ),
                value,  # fallback
            )
        return value

    seeds = [int(seed) for seed in re.findall(r"\d+", input_data[0])]
    locations = [lookup_location(seed) for seed in seeds]

    return min(locations)


def part2():
    input_data = open(__file__.rstrip("code.py") + "input.txt").read().splitlines()
    maps = []
    for line in input_data[2:]:
        if "map" in line:
            maps.append(dict())
        elif line != "":
            destination, source, length = [int(value) for value in line.split()]
            maps[-1][range(source, source + length)] = range(
                destination, destination + length
            )

    # The strategy used here is an improvement over a naive brute force approach,
    # but can be optimized by checking whole ranges at a time (while taking
    # into account where they 'split')
    def reverse_lookup_seed(location: int) -> int:
        value = location
        for current_map in reversed(maps):
            value = next(
                (
                    source_range.start + (value - destination_range.start)
                    for source_range, destination_range in current_map.items()
                    if value in destination_range
                ),
                value,  # fallback
            )
        return value

    initial_seed_data = [int(seed) for seed in re.findall(r"\d+", input_data[0])]
    seed_ranges = []
    for index in range(0, len(initial_seed_data) - 1, 2):
        start, length = initial_seed_data[index : index + 2]
        seed_ranges.append(range(start, start + length))

    location = 0
    while True:
        potential_seed = reverse_lookup_seed(location)
        if any(potential_seed in seed_range for seed_range in seed_ranges):
            return location
        location += 1


print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
