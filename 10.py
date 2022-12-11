TODO = False
SKIP = True
EXIT = True
TIME_IT = True
TEST = False
TEST_SHOW_DIFF = True
TEST_CASE_RESULT = """##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.####....####....####....####....####....#####.....#####.....#####.....#####.....######......######......######......###########.......#######.......#######....."""
TEST_CASE = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

def compute(what): # part 2
    i = [x for x in what.split('\n') if x]
    X = 1
    cycles = 0
    px = list("." * 40 * 6)

    def update(x, c, p):
        y = (c-1) % 40
        if y in (x-1, x, x+1):
            p[c-1] = "#"

    for x in i:
        cycles += 1
        update(X, cycles, px)
        if 'addx' in x:
            cycles += 1
            update(X, cycles, px)
            X += int(x.split()[1])

    # print("\n".join(["".join(px[y:y+40]) for y in range(0, len(px), 40)]))
    return "".join(px)

def compute_part1(what):
    i = [x for x in what.split('\n') if x]
    X = 1
    cycles = 0
    strengths = {}
    for x in i:
        cycles += 1
        strengths[cycles] = X * cycles
        if 'addx' in x:
            cycles += 1
            strengths[cycles] = X * cycles
            X += int(x.split()[1])

    return sum(strengths[x] for x in [20, 60, 100, 140, 180, 220])
