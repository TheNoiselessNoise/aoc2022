TODO = False
SKIP = True
EXIT = True
TIME_IT = True
TEST = False
TEST_SHOW_DIFF = True
TEST_CASE_RESULT = 70
TEST_CASE = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def compute(what):
    import string
    z = string.ascii_lowercase + string.ascii_uppercase
    l = what.split('\n')
    g = [l[x:x+3] for x in range(0, len(l), 3)]
    x = [set(z[0]) & set(z[1]) & set(z[2]) for z in g if z[0]]
    return sum(z.index(list(y)[0]) + 1 for y in x if len(y))

def compute_part1(what):
    import string
    z = string.ascii_lowercase + string.ascii_uppercase
    i = [(x[:len(x)//2], x[len(x)//2:]) for x in what.split('\n')]
    x = [set(x) & set(y) for x, y in i]
    return sum(z.index(list(y)[0]) + 1 for y in x if len(y))
