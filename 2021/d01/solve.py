import fileinput


def part1(lines):
    data = [int(line) for line in lines]
    return sum(a < b for a, b in zip(data, data[1:]))


def part2(lines):
    data = [int(line) for line in lines]
    windows = list(zip(data, data[1:], data[2:]))
    return sum(sum(a) < sum(b) for a, b in zip(windows, windows[1:]))


if __name__ == "__main__":
    lines = [line.strip() for line in fileinput.input()]
    print("part1", part1(lines))
    print("part2", part2(lines))
