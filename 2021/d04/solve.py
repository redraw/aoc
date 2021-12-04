import re
import itertools
import fileinput


def parse_input(lines):
    game, *raw_boards = lines.split("\n\n")
    numbers = [int(n) for n in game.split(",")]
    boards = [
        [[int(n) for n in re.findall(r"\b\d+\b", row)] for row in board.split("\n") if row] for board in raw_boards
    ]
    hits = [[[0 for _ in range(len(boards[0][0]))] for _ in range(len(boards[0]))] for _ in range(len(boards))]
    return numbers, boards, hits


def calculate_score(board, checkboard, number):
    result = 0
    for x_board, x_checkboard in zip(board, checkboard):
        for y_board, y_checkboard in zip(x_board, x_checkboard):
            if not y_checkboard:
                result += y_board
    return result * number


def part1(lines):
    numbers, boards, hits = parse_input(lines)

    for number in numbers:
        print(f"playing {number}")

        for b, board in enumerate(boards):
            for x, row in enumerate(board):
                for y, item in enumerate(row):
                    if number == item:
                        hits[b][x][y] = 1

            checkboard = hits[b].copy()

            if any(all(items) for items in itertools.chain(checkboard, zip(*checkboard))):
                print(f"winner is {b=}, row completed, {checkboard=}")
                return calculate_score(board, checkboard, number)


def part2(lines):
    pass


if __name__ == "__main__":
    lines = "".join([line for line in fileinput.input()])
    print("part1", part1(lines))
    print("part2", part2(lines))
