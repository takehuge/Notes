# import matplotlib
# matplotlib.use('tkAgg') # bring upfront # TO AVOID: RuntimeError: Python is not installed as a framework.

import time
# from pylab import linspace
from numpy import sin, cos, pi

def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

city = city_generator()

try:
    while True:
        print(next(city))
except:
    print("\nDone generating cities!")

def genum(n):
    for i in range(n):
        yield i
print(list(genum(37)))


def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(7)
for x in f:
    print(x)
print


def permutations(items):
    n = len(items)
    if n == 0:
        yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i] + items[i + 1:]):
                yield [items[i]] + cc

for p in permutations(['r', 'e', 'd']):
    time.sleep(0.0)
    print(''.join(p))
for p in permutations(list("game")):
    time.sleep(0.0)
    print(''.join(p))

def stepcalc(x, y ,z):
    yield x
    inp = 0
    while inp == 0:
        yield y
        inp = int(input("0/1?"))
    yield z
    

step = stepcalc(0, 1, 2) # make it an object first!
a = next(step)
print("a:", a)
print("a:", a)
print(next(step))
print(next(step))
print(next(step))
print(next(step))
step = stepcalc(10, 20 ,30) # RESET
print(next(step))
print(next(step))
print(next(step))
print(next(step))
print(next(step))
print(next(step))

