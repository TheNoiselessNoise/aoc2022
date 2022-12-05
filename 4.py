import os
import sys

TODO = False
SKIP = True
EXIT = True
TIME_IT = True
TEST = False
TEST_SHOW_DIFF = True
TEST_CASE_RESULT = 4
TEST_CASE = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def compute(what):
    i = [list(map(lambda y: y.split("-"), x.split(","))) for x in what.split('\n') if x]
    r = lambda y: list(range(int(y[0]), int(y[1]) + 1))
    j = [(r(y[0]), r(y[1])) for y in i]
    return sum(any(y in x[1] for y in x[0]) for x in j)

def compute_part1(what):
    i = [list(map(lambda y: y.split("-"), x.split(","))) for x in what.split('\n') if x]
    r = lambda y: list(range(int(y[0]), int(y[1]) + 1))
    j = [(r(y[0]), r(y[1])) for y in i]
    j = [(r[0], r[1]) if len(r[0]) <= len(r[1]) else (r[1], r[0]) for r in j]
    return sum(all(y in x[1] for y in x[0]) for x in j)
