import fileinput
from collections import Counter
from itertools import product


def debug(grid):
    print("-" * 10)
    for y in range(10):
        for x in range(10):
            value = grid[(x, y)]
            print("*" if value == 0 else value, end="")
        print()


def load_grid(payload):
    grid = {}
    for y, row in enumerate(payload):
        for x, value in enumerate(row):
            grid[(x, y)] = int(value)
    return grid


def kernel(x, y):
    return ((x + dx, y + dy) for dx, dy in product(range(-1, 2), range(-1, 2)))


def run_step(grid):
    flashed = []

    def increase(coord):
        grid[coord] += 1
        if grid[coord] > 9:
            grid[coord] = 0
            flashed.append(coord)

    for coord in grid:
        increase(coord)

    while flashed:
        x, y = flashed.pop()
        for coord in kernel(x, y):
            if coord in grid and grid[coord] != 0:
                increase(coord)


def part1(payload):
    grid = load_grid(payload)
    flashes = 0
    for _ in range(100):
        debug(grid)
        run_step(grid)
        values = grid.values()
        flashes += Counter(values).get(0, 0)
    return flashes


def part2(payload):
    grid = load_grid(payload)
    step = 0

    while True:
        run_step(grid)
        step += 1
        values = grid.values()
        if all(value == 0 for value in values):
            return step


if __name__ == "__main__":
    payload = [line.strip() for line in fileinput.input()]
    print("part1", part1(payload))
    print("part2", part2(payload))
