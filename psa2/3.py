from random import uniform
from math import pi


def three_acute_angles():
    l = 2 * pi
    p1 = uniform(0, l)
    p2 = uniform(0, l)
    while p2 == p1:
        p2 = uniform(0, l)
    p3 = uniform(0, l)
    while p3 == p1 or p3 == p2:
        p3 = uniform(0, l)
    p = [p1, p2, p3]
    p.sort()
    a1 = abs(p[0] - p[1]) / 2 * 57.2957795
    a2 = abs(p[1] - p[2]) / 2 * 57.2957795
    a3 = abs(p[0] + (l - p[2])) / 2 * 57.2957795
    if 90 > a1 and 90 > a2 and 90 > a3:
        return True
    return False


n_tests = 100_000
n = 0
for _ in range(n_tests):
    if three_acute_angles():
        n += 1

print(n / n_tests)