from .solve import part1, part2

TEST_INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678""".splitlines()


def test_part1():
    assert part1(TEST_INPUT) == 15


def test_part2():
    assert part2(TEST_INPUT) == 1134
