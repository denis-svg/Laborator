from random import uniform


def is_in_box():
    d = 175
    w = d * 2 * 8
    h = d * 2 * 8
    x = uniform(0, w)
    y = uniform(0, h)
    row1, col1 = x // (d * 2), y // (d * 2)
    x += d / 2
    y += d / 2
    row2, col2 = x // (d * 2), y // (d * 2)
    if row1 != row2 or col1 != col2:
        return False
    x -= d
    y -= d
    row2, col2 = x // (d * 2), y // (d * 2)
    if row1 != row2 or col1 != col2:
        return False
    return True


n_tests = 100_000
n = 0
for _ in range(n_tests):
    if is_in_box():
        n += 1

print(f"""probability of wining {n / n_tests}""")
print(f"""Expected value {1 * n / n_tests - 0.25 * (1 - n / n_tests)}""")
