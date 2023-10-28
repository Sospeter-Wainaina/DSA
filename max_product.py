import numpy as np


def max_product(array):
    array.sort(reverse=True)

    return f'max product of {array} is {array[0]*array[1]}'


#print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Method 2

def product_max(arr):
    max1, max2 = 0, 0
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i < max1:
            max2 = i
    return max1*max2


print(product_max([1, 2, 3, 4, 5, 6, 7, 8, 9]))
