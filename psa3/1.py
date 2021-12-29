from random import uniform


a = 1
c = 1
experiments = 10000
n = 0
for i in range(experiments):
    r = uniform(0, 1)
    b = 4 * r
    delta = b * b - 4 * a * c
    if delta > 0:
        n += 1
print(n / experiments)
