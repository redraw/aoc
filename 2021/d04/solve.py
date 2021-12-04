import re
import fileinput
from collections import namedtuple
from itertools import chain


TurnState = namedtuple("TurnState", "boards, number, board, fullboard, checkboard")


def parse_input(lines):
    game, *raw_boards = lines.split("\n\n")
    numbers = [int(n) for n in game.split(",")]
    boards = [
        [[int(n) for n in re.findall(r"\b\d+\b", row)] for row in board.split("\n") if row]
        for board in raw_boards  # noqa
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


def play(lines):
    numbers, boards, hits = parse_input(lines)

    for number in numbers:
        print(f"playing {number}")

        for board, fullboard in enumerate(boards):
            for x, row in enumerate(fullboard):
                for y, item in enumerate(row):
                    if number == item:
                        hits[board][x][y] = 1

            checkboard = hits[board].copy()

            yield TurnState(boards, number, board, fullboard, checkboard)


def part1(lines):
    for turn in play(lines):
        if any(all(items) for items in chain(turn.checkboard, zip(*turn.checkboard))):
            print(f"winner is {turn.board=}, row completed, {turn.checkboard=}")
            return calculate_score(turn.fullboard, turn.checkboard, turn.number)


def part2(lines):
    winners = set()
    for turn in play(lines):
        if any(all(items) for items in chain(turn.checkboard, zip(*turn.checkboard))):
            if turn.board not in winners:
                print(f"winner is {turn.board=}, row completed, {turn.checkboard=}")
                winners.add(turn.board)
                if len(winners) == len(turn.boards):
                    return calculate_score(turn.fullboard, turn.checkboard, turn.number)


if __name__ == "__main__":
    lines = "".join([line for line in fileinput.input()])
    print("part1", part1(lines))
    print("part2", part2(lines))
