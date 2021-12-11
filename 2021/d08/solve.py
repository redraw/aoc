import fileinput
from collections import Counter


DIGITS = [
    {"a", "b", "c", "e", "f", "g"},  # 0
    {"c", "f"},  # 1
    {"a", "c", "d", "e", "g"},  # 2
    {"a", "c", "d", "f", "g"},  # 3
    {"b", "c", "d", "f"},  # 4
    {"a", "b", "d", "f", "g"},  # 5
    {"a", "b", "d", "e", "f", "g"},  # 6
    {"a", "c", "f"},  # 7
    {"a", "b", "c", "d", "e", "f", "g"},  # 8
    {"a", "b", "c", "d", "f", "g"},  # 9
]


def parse_lines(payload):
    for line in payload:
        signal, output = line.split(" | ")
        yield signal, output


def part1(payload):
    unique_digits = [
        DIGITS[1],
        DIGITS[4],
        DIGITS[7],
        DIGITS[8],
    ]

    total = 0

    for signal, output in parse_lines(payload):
        for digit in output.split():
            if any(len(segments) == len(digit) for segments in unique_digits):
                total += 1

    return total


def part2(payload):
    # how many times does a segment lights up across all digits?
    segment_counter = {
        "a": 8,
        "b": 6,
        "c": 8,
        "d": 7,
        "e": 4,
        "f": 9,
        "g": 7,
    }

    key = lambda digit: "".join(sorted(digit))
    encode = lambda counter, digit: sum(counter[segment] for segment in digit)

    # sum counter for each digit configuration to get a UNIQUE fingerprint
    fingerprints = [encode(segment_counter, digit) for digit in DIGITS]

    outputs = []

    for signal, output in parse_lines(payload):
        signal_counter = Counter(signal)

        digits = {}
        for digit in signal.split():
            fingerprint = encode(signal_counter, digit)
            digits[key(digit)] = fingerprints.index(fingerprint)

        outputs.append(int("".join(str(digits[key(digit)]) for digit in output.split())))

    return sum(outputs)


if __name__ == "__main__":
    payload = [line.strip() for line in fileinput.input()]
    print("part1", part1(payload))
    print("part2", part2(payload))
