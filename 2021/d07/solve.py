import fileinput
from functools import lru_cache


def part1(payload):
    positions = [int(n) for n in payload[0].split(",")]
    @lru_cache
    def cost(n, pos):
        return abs(n - pos)
    return min(sum(cost(n, pos) for n in positions) for pos in range(min(positions), max(positions) + 1))


def part2(payload):
    positions = [int(n) for n in payload[0].split(",")]
    @lru_cache
    def cost(n, pos):
        return sum(range(abs(n - pos) + 1))
    return min(sum(cost(n, pos) for n in positions) for pos in range(min(positions), max(positions) + 1))


if __name__ == "__main__":
    payload = [line.strip() for line in fileinput.input()]
    print("part1", part1(payload))
    print("part2", part2(payload))
