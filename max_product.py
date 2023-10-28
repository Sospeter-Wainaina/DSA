import numpy as np


def max_product(array):
    array.sort(reverse=True)

    return f'max product of {array} is {array[0]*array[1]}'


print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9]))
