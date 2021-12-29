from random import choice, shuffle


def is_assigned():
    seats = [i for i in range(100)]
    shuffle(seats)
    available_seats = [i for i in range(100)]
    new_seats = [choice(available_seats)]
    available_seats.remove(new_seats[0])
    if new_seats[0] == seats[-1]:
        return False
    for i in range(1, 100):
        if seats[i] in new_seats:
            n_seat = choice(available_seats)
            new_seats.append(n_seat)
            available_seats.remove(n_seat)
            if new_seats[i] == seats[-1]:
                return False
        else:
            new_seats.append(seats[i])
            available_seats.remove(seats[i])
    return True


tests = 10_000
n = 0
for i in range(tests):
    if is_assigned():
        n += 1
print(n / tests)
