from numpy import *

def awesome(func):
    def wrap(x):
        z = cos(x)
        return func(z)
    return wrap

@awesome
def average(x):
    y = sum(x) / len(x)
    y = sin(y)
    return y