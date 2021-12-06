import fileinput
from collections import deque


def calculate(payload, days):
    state = [int(n) for n in payload[0].split(",") if n]
    counter = deque([state.count(timer) for timer in range(9)])
    for i in range(days):
        # i've seen this in reddit for a ruby solution,
        # never though about rotating the array! neat
        counter.rotate(-1)
        counter[6] += counter[-1]
    return sum(counter)


def part1(payload):
    return calculate(payload, 80)


def part2(payload):
    return calculate(payload, 256)


if __name__ == "__main__":
    payload = [line.strip() for line in fileinput.input()]
    print("part1", part1(payload))
    print("part2", part2(payload))
