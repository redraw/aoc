import fileinput


def part1(lines):
    horizontal = 0
    depth = 0

    for line in lines:
        move, n = line.split()
        if move == "forward":
            horizontal += int(n)
        elif move == "up":
            depth -= int(n)
        elif move == "down":
            depth += int(n)

    return horizontal * depth


def part2(lines):
    horizontal = 0
    aim = 0
    depth = 0

    for line in lines:
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
    lines = [line.strip() for line in fileinput.input()]
    print("part1", part1(lines))
    print("part2", part2(lines))
