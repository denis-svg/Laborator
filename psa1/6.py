from PIL import Image
from random import randint
from multiprocessing import Process
from time import time


def get_time(function):
    def calculate_time(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        print(f"""{function.__name__} has executed in {time() - start} seconds and the area is {result} squared miles""")
        return result
    return calculate_time


@get_time
def monte_carlo_method(pixels, width, height, tests):
    counter = 0
    RED = (255, 0, 0, 255)
    for i in range(tests):
        x = randint(0, width - 1)
        y = randint(0, height - 1)
        if pixels[x, y] == RED:
            counter += 1
    return counter / tests * 42


@get_time
def normal_method(pixels, width, height):
    counter = 0
    RED = (255, 0, 0, 255)
    for x in range(width):
        for y in range(height):
            if pixels[x, y] == RED:
                counter += 1

    return counter / (width * height) * 42


im = Image.open('danger_zone.png')
pixels = im.load()
width, height = im.size


t1 = Process(target=normal_method, args=(pixels, width, height))
t2 = Process(target=monte_carlo_method, args=(pixels, width, height, 10_000))
t1.start()
t2.start()
t1.join()
t2.join()
im.close()
