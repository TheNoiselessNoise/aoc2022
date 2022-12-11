TODO = False
SKIP = True
EXIT = True
TIME_IT = True
TEST = False
TEST_SHOW_DIFF = True
TEST_CASE_RESULT = 8
TEST_CASE = """
30373
25512
65332
33549
35390
"""

def compute(what): # part 2
    i = [list(map(int, list(x))) for x in what.split('\n') if x]
    w, h = len(i[0]), len(i)

    score = 0
    for x in range(1, h - 1):
        for y in range(1, w - 1):
            top = []
            for z in range(y, 0, -1):
                top.append(i[z - 1][x])
                if i[z - 1][x] >= i[y][x]:
                    break

            left = []
            for z in range(x, 0, -1):
                left.append(i[y][z - 1])
                if i[y][z - 1] >= i[y][x]:
                    break

            bottom = []
            for z in range(y, h - 1):
                bottom.append(i[z + 1][x])
                if i[z + 1][x] >= i[y][x]:
                    break

            right = []
            for z in range(x, w - 1):
                right.append(i[y][z + 1])
                if i[y][z + 1] >= i[y][x]:
                    break

            s = len(top) * len(left) * len(bottom) * len(right)
            if s > score:
                score = s

    return score

def compute_part1(what):
    i = [list(map(int, list(x))) for x in what.split('\n') if x]
    w, h = len(i[0]), len(i)

    v = 0
    for x in range(1, h - 1):
        for y in range(1, w - 1):
            tv = all(i[z - 1][x] < i[y][x] for z in range(y, 0, -1))
            lv = all(i[y][z - 1] < i[y][x] for z in range(x, 0, -1))
            bv = all(i[z + 1][x] < i[y][x] for z in range(y, h - 1))
            rv = all(i[y][z + 1] < i[y][x] for z in range(x, w - 1))
            if any([tv, bv, lv, rv]):
                v += 1

    return (w * 2 + (h * 2) - 4) + v
