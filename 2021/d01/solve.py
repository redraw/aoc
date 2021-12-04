import fileinput


def part1(payload):
    data = [int(line) for line in payload]
    return sum(a < b for a, b in zip(data, data[1:]))


def part2(payload):
    data = [int(line) for line in payload]
    windows = list(zip(data, data[1:], data[2:]))
    return sum(sum(a) < sum(b) for a, b in zip(windows, windows[1:]))


if __name__ == "__main__":
    payload = [line.strip() for line in fileinput.input()]
    print("part1", part1(payload))
    print("part2", part2(payload))
