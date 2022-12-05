import os
import sys

TODO = False
SKIP = True
EXIT = True
TIME_IT = True
TEST = False
TEST_SHOW_DIFF = True
TEST_CASE_RESULT = 12
TEST_CASE = """A Y
B X
C Z"""

def compute(what):
    x = "ABC XYZ".split()
    def outcome(a, b):
        i = x[0].index(a)
        if b == 'Y': return i+1+3
        if b == 'X': return ((i+2)%len(x[0]))+1+0
        return ((i+1)%len(x[0]))+1+6
    return sum([outcome(*y.split()) for y in what.split('\n') if y])

def compute_part1(what):
    x = "ABC XYZ".split()
    def outcome(a, b):
        if x[0].index(a) == x[1].index(b): return 3
        return 6 if any(a == c[1] and b == c[0] for c in "XC YA ZB".split()) else 0
    return sum([outcome(*y.split())+(x[1].index(y.split()[1])+1) for y in what.split('\n') if y])

