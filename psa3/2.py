from random import uniform
from math import pi, cos, sin
from math import sqrt


def get_coordinates1():
    theta = uniform(0, 1) * 2 * pi
    r = uniform(0, 10) + uniform(0, 10)
    if r >= 10:
        r = 20 - r
    return r * cos(theta), r * sin(theta)


tests = 10000
n = 0
for i in range(tests):
    x, y = get_coordinates1()
    if x > 0:
        n += 1
print(f"""it lands in the right half of the target {n / tests}""")

n = 0
for i in range(tests):
    x, y = get_coordinates1()
    if sqrt(x * x + y * y) < 5:
        n += 1
print(f"""its distance from the center is less than 5 inches {n / tests}""")

n = 0
for i in range(tests):
    x, y = get_coordinates1()
    if sqrt(x * x + y * y) > 5:
        n += 1
print(f"""its distance from the center is greater than 5 inches {n / tests}""")

n = 0
for i in range(tests):
    x, y = get_coordinates1()
    if sqrt((x - 0) * (x - 0) + (y - 5) * (y - 5)) < 5:
        n += 1
print(f"""it lands within 5 inches of the point (0, 5) {n / tests}""")

