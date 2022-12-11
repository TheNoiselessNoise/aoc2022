TODO = False
SKIP = True
EXIT = True
TIME_IT = True
TEST = False
TEST_SHOW_DIFF = True
TEST_CASE_RESULT = 19
TEST_CASE = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

def compute_it(what, n):
    return [len(set(what[x:x+n])) == n for x in range(len(what))].index(True) + n

def compute(what): # part 2
    return compute_it(what, 14)

def compute_part1(what):
    return compute_it(what, 4)
