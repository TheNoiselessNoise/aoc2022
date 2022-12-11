TODO = False
SKIP = True
EXIT = True
TIME_IT = True
TEST = False
TEST_SHOW_DIFF = True
TEST_CASE_RESULT = 36
TEST_CASE = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

def step(fr, to):
    dx = to[0] - fr[0]
    dy = to[1] - fr[1]
    if not dy and abs(dx) == 2:
        fr[0] += 1 if dx > 0 else -1
    elif not dx and abs(dy) == 2:
        fr[1] += 1 if dy > 0 else -1
    elif (abs(dy) == 2 and abs(dx) > 0) or (abs(dx) == 2 and abs(dy) > 0):
        fr[0] += 1 if dx > 0 else -1
        fr[1] += 1 if dy > 0 else -1
    return fr

def compute(what): # part 2
    i = [(x.split()[0], int(x.split()[1])) for x in what.split('\n') if x]
    m = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

    h, tails = [0, 0], [[0, 0] for _ in range(9)]
    steps = [set() for _ in range(9)]

    for d, l in i:
        for _ in range(l):
            h = [h[0] + m[d][0], h[1] + m[d][1]]
            for j in range(len(tails)):
                tails[j] = step(tails[j], h if j == 0 else tails[j - 1])
                steps[j].add(tuple(tails[j]))

    return len(steps[-1])

def compute_part1(what):
    i = [(x.split()[0], int(x.split()[1])) for x in what.split('\n') if x]
    m = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

    h, t = [0, 0], [0, 0]
    steps = set()

    for d, l in i:
        for _ in range(l):
            h = [h[0] + m[d][0], h[1] + m[d][1]]
            steps.add(tuple(step(t, h)))

    return len(steps)
