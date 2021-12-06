from .solve import part1, part2

TEST_INPUT = """3,4,3,1,2""".splitlines()


def test():
    assert part1(TEST_INPUT) == 5934
    assert part2(TEST_INPUT) == 26984457539
