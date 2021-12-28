from random import shuffle
import matplotlib.pyplot as plt


def get_neighbors(table, nr):
    neighbors = {}
    for i in range(nr):
        n = []
        if i == nr - 1:
            n.append(table[0])
            n.append(table[i - 1])
            neighbors[str(table[i])] = n
            break
        n.append(table[i + 1])
        n.append(table[i - 1])
        neighbors[str(table[i])] = n
    return neighbors


def not_sit(nr):
    table = [i for i in range(1, nr + 1)]
    shuffle(table)
    n1 = get_neighbors(table, nr)
    shuffle(table)
    n2 = get_neighbors(table, nr)
    for i in range(1, nr + 1):
        x1 = n1[str(i)]
        x2 = n2[str(i)]
        for j in x1:
            if j in x2:
                return False
    return True


x_axis = [i for i in range(6, 101)]
y_axis = []
for i in range(6, 101):
    n_tests = 100_000
    n = 0
    for _ in range(n_tests):
        if not_sit(i):
            n += 1

    y_axis.append(n / n_tests)

print(y_axis)
plt.plot(x_axis, y_axis)
plt.show()
