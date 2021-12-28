from random import choice
import matplotlib.pyplot as plt


def sum_3_rolls():
    face_values = [1, 2, 3, 4, 5, 6]
    x1 = choice(face_values)
    x2 = choice(face_values)
    x3 = choice(face_values)
    return x1 + x2 + x3


p = 0
i = 0
x_axis = []
y_axis = []
while p < 0.5:
    i += 1
    x_axis.append(i)
    n_tests = 10_000
    n = 0
    for _ in range(n_tests):
        for _ in range(i):
            if sum_3_rolls() == 14:
                n += 1
    p = n / n_tests
    y_axis.append(p)

plt.style.use("fivethirtyeight")
plt.bar(x_axis, y_axis)
plt.xlabel("Number of rolls")
plt.ylabel("Probability of winning")
plt.show()
