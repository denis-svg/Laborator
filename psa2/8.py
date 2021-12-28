from random import uniform


for i in range(1, 100):
    bank = 0
    for _ in range(50_000):
        bank -= i
        x = uniform(0, 1)
        j = 0
        h = uniform(0, 1)
        while h <= x:
            h = uniform(0, 1)
            j += 1
        bank += j - 1
    print(i, bank / 50_000)