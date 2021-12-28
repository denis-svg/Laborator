from random import choice
from random import randint


def spin_die(cases, slots):
    c = choice(cases)
    # simulate first person and get only cases when the person remains alive
    i = randint(0, slots - 1)
    while c[i] == 1:
        i = randint(0, slots - 1)
    # spin the revolver after the person before me remained alive
    c = choice(cases)
    if c[0] == 1:
        return True
    return False


def not_spin_die(cases, slots):
    c = choice(cases)
    # simulate first person and get only cases when the person remains alive
    i = randint(0, slots - 1)
    while c[i] == 1:
        i = randint(0, slots - 1)
    # do not spin the revolver after the person before me remained alive
    if i == slots - 1:
        if c[0] == 1:
            return True
        return False
    if c[i + 1] == 1:
        return True
    return False


""" 6 slots for bullets"""
print("----------------------------------------------- 6 bullets -----------------------------------------------------")
# adjacent
c1 = [[1, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0],
      [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 0, 1]]
tests = 100000
counter_spin = 0
counter_not_spin = 0
for _ in range(tests):
    if spin_die(c1, 6):
        counter_spin += 1
    if not_spin_die(c1, 6):
        counter_not_spin += 1

print(f"""spinning probability to die if adjacent is {counter_spin / tests}""")
print(f"""not spinning probability to die if adjacent is {counter_not_spin / tests}\n""")

# single space in between
c2 = [[1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0],
      [0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1]]

tests = 100000
counter_spin = 0
counter_not_spin = 0
for _ in range(tests):
    if spin_die(c2, 6):
        counter_spin += 1
    if not_spin_die(c2, 6):
        counter_not_spin += 1

print(f"""spinning probability to die if there is single space in between is {counter_spin / tests}""")
print(f"""not spinning probability to die if there is single space in between is {counter_not_spin / tests}\n""")

# two spaces in between
c3 = [[1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1]]

tests = 100000
counter_spin = 0
counter_not_spin = 0
for _ in range(tests):
    if spin_die(c3, 6):
        counter_spin += 1
    if not_spin_die(c3, 6):
        counter_not_spin += 1

print(f"""spinning probability to die if there is two spaces in between is {counter_spin / tests}""")
print(f"""not spinning probability to die if there is two spaces in between is {counter_not_spin / tests}\n""")


""" 5 slots for bullets"""
print("----------------------------------------------- 5 bullets -----------------------------------------------------")
# adjacent
c1 = [[1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0],
      [0, 0, 0, 1, 1], [1, 0, 0, 0, 1]]
tests = 100000
counter_spin = 0
counter_not_spin = 0
for _ in range(tests):
    if spin_die(c1, 5):
        counter_spin += 1
    if not_spin_die(c1, 5):
        counter_not_spin += 1

print(f"""spinning probability to die if adjacent is {counter_spin / tests}""")
print(f"""not spinning probability to die if adjacent is {counter_not_spin / tests}\n""")

# single space in between
c2 = [[1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1],
      [1, 0, 0, 1, 0], [0, 1, 0, 0, 1]]
tests = 100000
counter_spin = 0
counter_not_spin = 0
for _ in range(tests):
    if spin_die(c2, 5):
        counter_spin += 1
    if not_spin_die(c2, 5):
        counter_not_spin += 1

print(f"""spinning probability to die if there is  space in between is {counter_spin / tests}""")
print(f"""not spinning probability to die if there is space in between is {counter_not_spin / tests}\n""")

