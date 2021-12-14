import fileinput
from functools import reduce

PAIRS = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}


def check_line(line):
    stack = []
    for char in line:
        if char in PAIRS.keys():
            stack.append(char)
        else:
            expected = PAIRS[stack.pop()]
            if char != expected:
                return char


def part1(payload):
    score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    errors = []
    for line in payload:
        if err := check_line(line):
            errors.append(err)

    return sum(score.get(err) for err in errors)


def complete_sequence(line):
    stack = []
    sequence = []

    for char in line:
        if char in PAIRS.keys():
            stack.append(char)
        else:
            stack.pop()

    while stack:
        sequence.append(PAIRS[stack.pop()])

    return sequence


def part2(payload):
    score = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    incompletes = [line for line in payload if not check_line(line)]
    closing_sequences = [complete_sequence(line) for line in incompletes]

    scores = [reduce(lambda total, char: total * 5 + score[char], seq, 0) for seq in closing_sequences]

    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    payload = [line.strip() for line in fileinput.input()]
    print("part1", part1(payload))
    print("part2", part2(payload))
