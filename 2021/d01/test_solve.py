from .solve import part1, part2

TEST_INPUT = """199
200
208
210
200
207
240
269
260
263
""".splitlines()


def test_part1():
    assert part1(TEST_INPUT) == 7


def test_part2():
    assert part2(TEST_INPUT) == 5
