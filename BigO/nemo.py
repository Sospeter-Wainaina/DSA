# Big O notation
import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill',
            'bloat', 'nigel', 'squirt', 'darla', 'hank']


def findNemo(array):
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('FOUND NEMO !')


findNemo(everyone)  # O(n) -- Linear Time to find Nemo
# The BigO depends on the number of inputs

Boxes = [1, 2, 3, 4, 5, 6]


def first_item(items):
    print(f'The first item is {items[0]} ')


first_item(Boxes)  # O(1) Constant Time


def logFirstTwo(items):
    print(f'The first item is {items[0]} ')  # O(1)
    print(f'The first item is {items[1]} ')  # O(1)


# O(2) no matter how many items in the array, it will always be 2 operations
logFirstTwo(boxes)


def anotherFunctionChallange():
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)
    for i in range(0, n):
        x = i + 1  # O(n)
        y = i + 2  # O(n)
        z = i + 3  # O(n)
    for j in range(0, n):
        p = j * 2  # O(n)
        q = j * 2  # O(n)
    whoAmI = "I don't know"  # O(1)

# Big O(4 + 5n) = O(n)

# Rule Book
# Rule 1: Worst Case
# BigO only cares about the worstcase scenario
# rule 2: Remove Constants
# O(2n) = O(n)
# RULE 3: Different terms for inputs


def compressBoxesTwice(boxes, boxes2):
    for i in boxes:  # O(a)
        print(i)
    for j in boxes2:  # O(b)
        print(j)
