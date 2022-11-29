"""
Contains utils for dealing with bits
"""


def get_2c_repr_n(num, l):
    return ((1 << l) - 1) & num


def get_2c_repr_byte(num):
    return ((1 << 8) - 1) & num


def get_2c_repr_short(num):
    return ((1 << 16) - 1) & num


def get_2c_repr_int(num):
    return ((1 << 32) - 1) & num


def get_2c_repr_long(num):
    return ((1 << 64) - 1) & num


if __name__ == '__main__':
    print('Testing bit utils')
    print(bin(get_2c_repr_n(5, 4)))
    print(bin(get_2c_repr_n(-5, 4)))
    print()
    for i in range(0, 10):
        print(i, bin(get_2c_repr_byte(i)), bin(get_2c_repr_short(i)),
              bin(get_2c_repr_int(i)), bin(get_2c_repr_long(i)))
        print(-i, bin(get_2c_repr_byte(-i)), bin(get_2c_repr_short(-i)),
              bin(get_2c_repr_int(-i)), bin(get_2c_repr_long(-i)))
