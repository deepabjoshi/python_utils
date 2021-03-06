"""

"""


import itertools as it


def is_prime(i, primes):
    idx = 0
    while idx < len(primes) and primes[idx] ** 2 <= i:
        if i % primes[idx] == 0:
            i_is_prime = False
            break
        idx += 1
    else:
        # Example: else in loops
        i_is_prime = i >= 2
    return i_is_prime


def sequence_generator_6k_plus_minus_one(k=1):
    """ Generates a sequence of numbers 6k +- 1. K decides the starting position - default 1.
    """
    for i in it.count(6 * k, 6):
        yield i - 1
        yield i + 1


def prime_generator_infinite():
    yield 2
    yield 3
    primes = [2, 3]
    for i in sequence_generator_6k_plus_minus_one():
        if is_prime(i, primes):
            primes.append(i)
            yield i


def prime_generator_finite(n):
    for p in prime_generator_infinite():
        if p > n: break
        yield p


def is_prime_with_gen(i):
    primes = []
    for p in prime_generator_infinite():
        if p ** 2 > i:
            break
        primes.append(p)
    return is_prime(i, primes)


def find_prime_factors(num, prime_list, prime_gen):
    factors = []
    while len(prime_list) == 0 or prime_list[-1] * prime_list[-1] < num:
        prime_list.append(next(prime_gen))

    idx = 0
    n = num
    p = prime_list[idx]
    while (n > 1) and (p * p <= num):
        # print('Begin loop:', num, n, p, factors)
        if n % p == 0:
            factors.append(p)
            n //= p
        else:
            idx += 1
            p = prime_list[idx]
        # print('End loop:', num, n, p, factors)
    if n > 1:
        factors.append(n)
    return factors


if __name__ == '__main__':
    prime_list = []
    prime_gen = prime_generator_infinite()
    print(5, find_prime_factors(5, prime_list, prime_gen), prime_list)
    for i in range(2, 21):
        if is_prime(i, [2, 3, 5]):
            print('Prime:', i)
        else:
            print('Composite:', i, find_prime_factors(i, prime_list, prime_gen), prime_list)
