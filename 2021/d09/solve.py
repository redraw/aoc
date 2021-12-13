import fileinput
from functools import reduce


def load_heightmap(payload):
    heightmap = {}
    for y, row in enumerate(payload):
        for x, height in enumerate(row):
            heightmap[(x, y)] = int(height)
    return heightmap


def find_lows(heightmap):
    lows = []

    for coords, height in heightmap.items():
        x, y = coords
        neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        if all(height < heightmap.get(neighbour, 10) for neighbour in neighbours):
            lows.append(coords)

    return lows


def part1(payload):
    heightmap = load_heightmap(payload)
    lows = find_lows(heightmap)

    return sum(heightmap[low] + 1 for low in lows)


def walk_basin(heightmap, low) -> int:
    basin = set([low])
    stack = [low]
    while stack:
        x, y = stack.pop()
        neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for neighbour in neighbours:
            height = heightmap.get(neighbour, 0)
            if heightmap[(x, y)] < height and height != 9:
                stack.append(neighbour)
                basin.add(neighbour)
    return len(basin)


def part2(payload):
    heightmap = load_heightmap(payload)
    lows = find_lows(heightmap)
    basins = sorted([walk_basin(heightmap, low) for low in lows], reverse=True)

    return reduce(lambda x, y: x * y, basins[:3])


if __name__ == "__main__":
    payload = [line.strip() for line in fileinput.input()]
    print("part1", part1(payload))
    print("part2", part2(payload))
