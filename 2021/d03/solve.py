import fileinput


def part1(lines):
    # transpose bits
    T = list(zip(*lines))
    # count
    gamma = "".join("1" if column.count("1") > column.count("0") else "0" for column in T)
    epsilon = "".join("1" if column.count("1") < column.count("0") else "0" for column in T)
    # convert to decimal, and mult
    return int(gamma, 2) * int(epsilon, 2)


def compressor(data, kind):
    compressed = list(data)
    idx = 0
    while len(compressed) > 1:
        T = list(zip(*compressed))
        col = T[idx]
        most_common = "1" if col.count("1") >= col.count("0") else "0"
        least_common = "0" if col.count("1") >= col.count("0") else "1"
        if kind == "oxygen":
            target = most_common
        elif kind == "co2":
            target = least_common
        compressed = [row for row in compressed if row[idx] == target]
        idx += 1
    return compressed[0]


def part2(lines):
    oxygen = compressor(lines, kind="oxygen")
    co2 = compressor(lines, kind="co2")
    return int(oxygen, 2) * int(co2, 2)


if __name__ == "__main__":
    lines = [line.strip() for line in fileinput.input()]
    print("part1", part1(lines))
    print("part2", part2(lines))
