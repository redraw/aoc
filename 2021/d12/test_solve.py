from .solve import part1, part2

TEST_INPUT_1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()

TEST_INPUT_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".splitlines()

TEST_INPUT_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""".splitlines()


def test_part1():
    assert part1(TEST_INPUT_1) == 10
    assert part1(TEST_INPUT_2) == 19
    assert part1(TEST_INPUT_3) == 226


def test_part2():
    assert part2(TEST_INPUT_1) == 36
    assert part2(TEST_INPUT_2) == 103
    assert part2(TEST_INPUT_3) == 3509
