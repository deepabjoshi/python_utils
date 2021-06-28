"""
Contains utility functions for digits in a number. Decimal digits 0-9 are assumed in this module.
"""


def get_digits(num):
    if num == 0:
        return [0]
    digits = []
    while num > 0:
        num, d = divmod(num, 10)
        digits.append(d)
    digits.reverse()
    return digits


def get_num(digits):
    num = 0
    for d in digits:
        num = num * 10 + d
    return num


def right_rotate_digits_gen(num, rotations=None):
    num_digits = len(str(num))
    multiplier = pow(10, num_digits - 1)
    if not rotations:
        rotations = num_digits
    for i in range(0, rotations):
        q, r = divmod(num, 10)
        num = q + r * multiplier
        yield num


if __name__ == '__main__':
    print('get_digits(1234) = ', get_digits(1234))
    print('get_digits(555) = ', get_digits(555))
    print('get_digits(6) = ', get_digits(6))
    print('get_digits(0) = ', get_digits(0))
    print('get_digits(10) = ', get_digits(10))

    print('get_num([1, 6, 5, 4]) =', get_num([1, 6, 5, 4]))
    print('get_num([2, 3, 3]) =', get_num([2, 3, 3]))
    print('get_num([0, 6, 9]) =', get_num([0, 6, 9]))

    print('Rotations of 1021:')
    for r in right_rotate_digits_gen(1021):
        print(r)
    print('Rotations of 3:')
    for r in right_rotate_digits_gen(3):
        print(r)
    print('2 Rotations of 666:')
    for r in right_rotate_digits_gen(666, 2):
        print(r)
    print('4 Rotations of 9:')
    for r in right_rotate_digits_gen(9, 4):
        print(r)
