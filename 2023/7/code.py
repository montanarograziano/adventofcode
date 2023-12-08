# Advent of code Year 2023 Day 7 solution
# Author = montanarograziano
# Date = December 2023
from collections import Counter

map_hand = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

map_part2 = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14,
    "J": 1,
}


def point(hand):
    if len(set(hand)) == 2:
        if Counter(hand).most_common(1)[0][1] == 4:
            return 2
        else:
            return 3
    elif len(set(hand)) == 3:
        if Counter(hand).most_common(1)[0][1] == 3:
            return 4
        elif Counter(hand).most_common(1)[0][1] == 2:
            return 5
    elif len(set(hand)) == 4:
        return 6
    elif len(set(hand)) == 5:
        return 7
    else:
        return 1


def part2():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = input_file.readlines()
        hands = []
        r = []
        for i, l in enumerate(input):
            line = l.strip()
            chars, bid = line.split(" ")
            hand = list(map(lambda x: map_part2[x], chars))
            original_hand = hand.copy()
            if 1 in hand:
                cnt = Counter(hand)
                if cnt[1] != 5:
                    del cnt[1]
                    most_common, freq = cnt.most_common(1)[0]
                    if freq == 1:
                        most_common = sorted(hand, reverse=True)[0]

                    hand = [h if h != 1 else most_common for h in hand]

            hands.append(hand)
            rank_with_bid = (point(hand), original_hand, bid)
            r.append(rank_with_bid)

        r.sort(key=lambda x: (-x[0], x[1]))
        tot = 0
        for i, x in enumerate(r):
            tot += (i + 1) * int(x[2])
    return tot


def part1():
    with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
        input = input_file.readlines()
        hands = []
        r = []
        for i, l in enumerate(input):
            line = l.strip()
            chars, bid = line.split(" ")
            hand = list(map(lambda x: map_hand[x], chars))
            hands.append(hand)
            rank_with_bid = (point(hand), hand, bid)
            r.append(rank_with_bid)

        r.sort(key=lambda x: (-x[0], x[1]))
        tot = 0
        for i, x in enumerate(r):
            tot += (i + 1) * int(x[2])
    return tot


print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
