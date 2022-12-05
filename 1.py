import os
import sys

TODO = False
SKIP = True
EXIT = True
TIME_IT = True
TEST = False
TEST_SHOW_DIFF = True
TEST_CASE_RESULT = 24000
TEST_CASE = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def compute(what):
    x = [sum([int(y) for y in x.split('\n') if y]) if '\n' in x else int(x) for x in what.split('\n\n')]
    return sum(sorted(x, reverse=True)[0:3])

def compute_part1(what):
    return max(sum([int(y) for y in x.split('\n') if y]) if '\n' in x else int(x) for x in what.split('\n\n'))
