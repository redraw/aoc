from .solve import part1, part2

TEST_INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".splitlines()


def test_part1():
    assert part1(TEST_INPUT) == 1656


def test_part2():
    assert part2(TEST_INPUT) == 195
