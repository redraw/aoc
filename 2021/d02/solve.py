import fileinput


def part1(payload):
    horizontal = 0
    depth = 0

    for line in payload:
        move, n = line.split()
        if move == "forward":
            horizontal += int(n)
        elif move == "up":
            depth -= int(n)
        elif move == "down":
            depth += int(n)

    return horizontal * depth


def part2(payload):
    horizontal = 0
    aim = 0
    depth = 0

    for line in payload:
        move, n = line.split()
        if move == "forward":
            horizontal += int(n)
            depth += int(n) * aim
        elif move == "up":
            aim -= int(n)
        elif move == "down":
            aim += int(n)

    return horizontal * depth


if __name__ == "__main__":
    payload = [line.strip() for line in fileinput.input()]
    print("part1", part1(payload))
    print("part2", part2(payload))
