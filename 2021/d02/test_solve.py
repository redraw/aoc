from .solve import part1, part2

TEST_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()


def test_part1():
    assert part1(TEST_INPUT) == 150


def test_part2():
    assert part2(TEST_INPUT) == 900
