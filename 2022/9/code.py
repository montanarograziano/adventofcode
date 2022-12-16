# Advent of code Year 2022 Day 9 solution
# Author = ?
# Date = December 2018

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def update(self, x: int, y: int):
        self.x += x
        self.y += y

    def current(self) -> tuple:
        current = (self.x, self.y)
        return current

    def update_tail(self, head, dir):
        head_x = head[0]
        head_y = head[1]
        if head_x == self.x:
            if head_y == self.y + 2:
                self.update(0, 1)
            elif head_y == self.y - 2:
                self.update(0, -1)
        if head_y == self.y:
            if head_x == self.x + 2:
                self.update(1, 0)
            elif head_x == self.x - 2:
                self.update(-1, 0)
        if head_x != self.x and head_y != self.y:
            if max(abs(head_x - self.x), abs(head_y - self.y)) > 1:
                new_x = head_x - self.x
                new_y = head_y - self.y
                self.update(new_x // abs(new_x), new_y // abs(new_y))


def part1(input):
    lines = input.split('\n')
    current_head = Position(0, 0)
    current_tail = Position(0, 0)
    visited = set()
    for line in lines:
        direction, steps = line.split(" ")[0], int(line.split(" ")[1])

        match direction:
            case 'L':
                for i in range(steps):
                    current_head.update(0, -1)
                    current_tail.update_tail(current_head.current(), 'L')
                    visited.add(current_tail.current())

            case 'R':
                for i in range(steps):
                    current_head.update(0, 1)
                    current_tail.update_tail(current_head.current(), 'R')
                    visited.add(current_tail.current())
            case 'U':
                for i in range(steps):
                    current_head.update(-1, 0)
                    current_tail.update_tail(current_head.current(), 'U')
                    visited.add(current_tail.current())
            case 'D':
                for i in range(steps):
                    current_head.update(1, 0)
                    current_tail.update_tail(current_head.current(), 'D')
                    visited.add(current_tail.current())

    visited = sorted(visited)
    return len(visited)


print("Part One : " + str(part1(input)))

print("Part Two : " + str(None))
