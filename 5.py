TODO = False
SKIP = True
EXIT = True
TIME_IT = True
TEST = False
TEST_SHOW_DIFF = True
TEST_CASE_RESULT = "MCD"
TEST_CASE = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def compute_it(what, order=False):
    order = 1 if order else -1
    i = [x for x in what.split('\n\n') if x]
    c = [x[1::4] for x in i[0].split('\n')[:-1]]
    c = ["".join([y[x] for y in c]).strip() for x in range(len(c[0]))]
    m = [list(map(int, x.split()[1::2])) for x in i[1].split('\n') if x]
    for mv in m:
        c[mv[2] - 1] = c[mv[1] - 1][:mv[0]][::order] + c[mv[2] - 1]
        c[mv[1] - 1] = c[mv[1] - 1][mv[0]:]
    return "".join(x[0] for x in c)

def compute(what): # part 2
    return compute_it(what, True)

def compute_part1(what):
    return compute_it(what)
