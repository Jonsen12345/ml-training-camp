import numpy as np


def myfunc(a):
    useless_number = 2
    b = a
    c = call_func(b)
    print(1 / c)


def call_func(x):
    return x


if __name__ == '__main__':
    myfunc(10)
    myfunc(0)