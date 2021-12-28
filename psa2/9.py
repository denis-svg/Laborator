from random import choice

t = [0] * 99
t.append(1)

policies = 1000
claims = 0

for i in range(policies):
    if choice(t) == 1:
        claims += 1

print(claims)

print(int(policies/(1/0.01)))