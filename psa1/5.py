from hashlib import md5
import os
import math
from multiprocessing import Process


def main(bit_range, probability, tests, show=True):
    collision_count = 0
    # Each space_size counts for 4 bits, hence we have
    space_size = bit_range//4
    for i in range(tests):
        lookup_table = {}
        # find n by approximation using a formula from wikipedia
        n = int(math.sqrt(2 * (2 ** bit_range) * (-1) * math.log(1 - probability)))
        collision = False
        for _ in range(n):
            random_binary = os.urandom(bit_range // 8 + 2)
            result = md5(random_binary).hexdigest()
            result = result[:space_size]
            if result in lookup_table:
                collision_count += 1
                collision = True
                break
            else:
                lookup_table[result] = random_binary
        if collision and show:
            print("collision has occured")
        elif show:
            print("collision has not occured")

    print(f"""The probability of collisions is {collision_count / tests}""")


def main_in_threading(n_threads, bit_range, probability, tests):
    threads = []
    for i in range(n_threads):
        threads.append(Process(target=main, args=(bit_range, probability, tests, False)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


# main_in_threading(10, 40, 0.5, 10)
main(40, 0.5, 50)
