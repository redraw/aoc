from .solve import part1, part2

TEST_INPUT = """16,1,2,0,4,2,7,1,2,14""".splitlines()


def test_part1():
    assert part1(TEST_INPUT) == 37


def test_part2():
    assert part2(TEST_INPUT) == 168
