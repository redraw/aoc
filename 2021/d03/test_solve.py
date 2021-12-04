from .solve import part1, part2

TEST_INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()


def test():
    assert part1(TEST_INPUT) == 198
    assert part2(TEST_INPUT) == 230
