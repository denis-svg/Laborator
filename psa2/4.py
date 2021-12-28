from random import uniform
from math import sqrt


def real_roots():
    a = 1
    b = uniform(-1, 1)
    c = uniform(-1, 1)
    if b * b - 4 * a * c > 0:
        return True
    return False


def positive_roots():
    a = 1
    b = uniform(-1, 1)
    c = uniform(-1, 1)
    while b * b - 4 * a * c < 0:
        b = uniform(-1, 1)
        c = uniform(-1, 1)
    delta = sqrt(b * b - 4 * a * c)
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    if x1 > 0 and x2 > 0:
        return True
    return False


n_tests = 10_000
n_real = 0
n_positive = 0
for _ in range(n_tests):
    if real_roots():
        n_real += 1
    if positive_roots():
        n_positive += 1

print(f"""real roots {n_real / n_tests}\npositive roots {n_positive / n_tests}""")
