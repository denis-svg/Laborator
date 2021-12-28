from random import choice
import matplotlib.pyplot as plt

p = [0, 1]
interval = [i for i in range(35, 66)]
tosses = 100
experiments = 1000
recorder = {}
for i in interval:
    recorder[str(i)] = 0


for j in range(experiments):
    n = 0
    for i in range(tosses):
        if choice(p) == 1:
            n += 1
    if n in interval:
        recorder[str(n)] += 1

y_axis = []
for i in interval:
    y_axis.append(recorder[str(i)])
plt.bar(interval, y_axis)
plt.show()

