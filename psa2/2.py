from random import uniform


def is_triangle(a, b, c):
    if a + b < c:
        return False
    if a + c < b:
        return False
    if b + c < a:
        return False
    return True


def get_sides():
    a = uniform(0, 1)
    b = 1 - a
    if a > b:
        c = uniform(0, a)
        a -= c
    else:
        c = uniform(0, b)
        b -= c

    return a, b, c


n_tests = 10_000
n = 0
for i in range(n_tests):
    a, b, c = get_sides()
    if is_triangle(a, b, c):
        n += 1

print(n / n_tests)
