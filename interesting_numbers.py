"""
Contains generators for various interesting number series such as triangular numbers, square numbers,
fibonacci numbers, factorials etc. Please note that all these are infinite. Finite generators could
be created from these using conditions.
"""


import itertools as it


def triangular_number_gen():
    tnum = 0
    for i in it.count(1):
        tnum += i
        yield tnum


def square_number_gen():
    for i in it.count(1):
        yield i * i


def fibonacci_number_gen():
    n1 = 1
    yield n1
    n2 = 1
    yield n2
    while True:
        n3 = n1 + n2
        yield n3
        n1, n2 = n2, n3


def factorial_gen():
    fact = 1
    for i in it.count(1):
        fact *= i
        yield fact


def pentagonal_number_gen():
    for i in it.count(1):
        yield (i * (3 * i - 1)) // 2


def hexagonal_number_gen():
    for i in it.count(1):
        yield i * (2 * i - 1)


def heptagonal_number_gen():
    for i in it.count(1):
        yield (i * (5 * i - 3)) // 2


def octagonal_number_gen():
    for i in it.count(1):
        yield i * (3 * i - 2)


if __name__ == '__main__':
    t = triangular_number_gen()
    s = square_number_gen()
    f = fibonacci_number_gen()
    v = factorial_gen()
    p = pentagonal_number_gen()
    h = hexagonal_number_gen()
    j = heptagonal_number_gen()
    o = octagonal_number_gen()
    for i in range(10):
        print(next(t), next(s), next(f), next(v), next(p), next(h), next(j), next(o))
