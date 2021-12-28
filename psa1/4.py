from random import randint

line = input().split()

# simulation
n = int(line[0])
k = int(line[1])
max_pts = int(line[2])

# simulation
tests = 100000
counter = 0
for _ in range(tests):
    points = 0
    while points < k:
        points += randint(1, max_pts)
    if points <= n:
        counter += 1

print(counter / tests)


# recursive
def p(s, j):
    global m
    if s >= k:
        if s <= n:
            m += 1 / (max_pts ** j)
    else:
        for h in range(1, max_pts + 1):
            p(s + h, j + 1)


m = 0
p(0, 0)

print(m)
