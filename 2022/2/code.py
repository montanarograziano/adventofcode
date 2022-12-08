# Advent of code Year 2022 Day 2 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()

points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
respective = {'A': 'X', 'B': 'Y', 'C': 'Z'}
wins_against = {'A': 'Z', 'B': 'X', 'C': 'Y'}
lose_against = {'A': 'Y', 'B': 'Z', 'C': 'A'}
total = 0
total2 = 0
hands = input.split('\n')
for h in hands:
    a = h.split(" ")[0]
    b = h.split(" ")[1]
    # Draw scenario
    if points[b] == points[a]:
        total += 3 + points[b]
    # Opponent wins
    elif b == wins_against[a]:
        total += points[b]
    # I win
    else:
        total += 6 + points[b]

for h in hands:
    a = h.split(" ")[0]
    b = h.split(" ")[1]
    match b:
        case 'X':
            my_hand = wins_against[a]
            total2 += points[my_hand]
        case 'Y':
            my_hand = respective[a]
            total2 += 3 + points[my_hand]
        case 'Z':
            my_hand = lose_against[a]
            total2 += 6 + points[my_hand]

print("Part One : " + str(total))

print("Part Two : " + str(total2))
