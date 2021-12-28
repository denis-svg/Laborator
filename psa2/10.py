from random import choice

rides = 365 * 2
# paying 2 dollars

print(f"""expected cost if he pays is {rides * 2}$ per ride""")


# doesn't pay 2 dollars
t = [0] * 95 + [1] * 5
h = [0] * 98 + [1] * 2
cost = 0
n_caught = 0
for i in range(rides):
    if choice(h) == 1:
        cost += 2
        continue
    if choice(t) == 1 and n_caught == 0:
        cost += 50
        n_caught += 1
        continue
    if choice(t) == 1 and n_caught == 1:
        cost += 150
        n_caught += 1
        continue
    if choice(t) == 1 and n_caught > 1:
        cost += 300
        n_caught += 1
        continue

print(f"""expected cost if he doesn't pay is {cost}$ per ride""")
