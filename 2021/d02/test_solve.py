from .solve import part1, part2

TEST_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()


def test():
    assert part1(TEST_INPUT) == 150
    assert part2(TEST_INPUT) == 900
