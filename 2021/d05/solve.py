import fileinput
from dataclasses import dataclass
from collections import defaultdict
from itertools import product


@dataclass
class Vent:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def x_dir(self):
        return 1 if self.x1 < self.x2 else -1

    @property
    def y_dir(self):
        return 1 if self.y1 < self.y2 else -1


def parse_vents(lines):
    for line in lines:
        coord1, coord2 = line.split(" -> ")
        x1, y1 = [int(n) for n in coord1.split(",")]
        x2, y2 = [int(n) for n in coord2.split(",")]
        yield Vent(x1, y1, x2, y2)


def part1(payload):
    board = defaultdict(int)
    for vent in parse_vents(payload):
        xr = range(vent.x1, vent.x2 + vent.x_dir, vent.x_dir)
        yr = range(vent.y1, vent.y2 + vent.y_dir, vent.y_dir)
        if vent.y1 == vent.y2 or vent.x1 == vent.x2:
            for x, y in product(xr, yr):
                board[(x, y)] += 1
    return sum(value > 1 for value in board.values())


def part2(payload):
    board = defaultdict(int)
    for vent in parse_vents(payload):
        xr = range(vent.x1, vent.x2 + vent.x_dir, vent.x_dir)
        yr = range(vent.y1, vent.y2 + vent.y_dir, vent.y_dir)
        if vent.y1 == vent.y2 or vent.x1 == vent.x2:
            for x, y in product(xr, yr):
                board[(x, y)] += 1
        elif abs(vent.x2 - vent.x1) == abs(vent.y2 - vent.y1):
            for x, y in zip(xr, yr):
                board[(x, y)] += 1
    return sum(value > 1 for value in board.values())


if __name__ == "__main__":
    payload = [line.strip() for line in fileinput.input()]
    print("part1", part1(payload))
    print("part2", part2(payload))
