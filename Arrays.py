import array as a
import numpy as np
print("Hello World")
# One DImensional Array
# an Array with a bunch of values (Same type) having being declared with single index

my_array = a.array('i')  # ----------------------->O(1)
print(my_array)
my_array1 = a.array('i', [1, 2, 3, 4])  # ----------------------->O(N)
print(my_array1)

np_array = np.array([], dtype=int)  # ----------------------->O(1)
print(np_array)

my_array2 = a.array('i', [1, 2, 3, 4])  # ----------------------->O(N)
print(my_array2)

# Inserting into an Array
my_array2.insert(4, 7)
print(my_array2)

# Traversing array


def traverseArray(Array):
    for i in Array:  # --------------O(n)
        print(i)  # -----------------O(1)


traverseArray(my_array2)

# Access elemens of an array


def accessElement(array, index):
    if index >= len(array):  # -----------------------------------O(1)
        print("There is not any element with that index")  # -----O(1)
    else:
        print(f"Your element is {array[index]}")  # --------------O(1)


accessElement(my_array2, 5)
# Time Complexity : O(1)
# Space Complexiy : O(1)

# Searching for an elemen in an array


def linearSearch(array, n):
    for i in range(0, len(array)):  # ------------------O(n)
        if array[i] == n:  # ---------------------------O(1)
            print(f"Your element is on index {i}")  # --O(1)
    return -1  # ---------------------------------------O(1)


linearSearch(my_array2, 7)
# Time complexity = O(n)
# Space Complexity= O(1) additional memory is not required to perform this operation

# Delete an element of an array
my_array2.remove(7)

print(my_array2)
# if you rmove an elemen from the middle of the array the time complexity will be O(n)
# Otherwise if you remove it from the end it will be O(1)
# Space complexity O(1)

# Append an array. Add a new element at the end of the array
my_array2.append(7)
print(my_array2)

# insert a number to an array

my_array2.insert(0, 9)
print(my_array2)

# Extend an array
arr_1 = a.array('i', [6, 7, 8, 9, 10])
print(arr_1)
my_array2.extend(arr_1)
print(my_array2)
# Array from list

tempList = [20, 21, 22, 23]
my_array2.fromlist(tempList)
print(my_array2)
# Remove last element with Pop
my_array2.pop()
print(my_array2)

# Reverse the array using reverse method
my_array2.reverse()
print(my_array2)
# Count method
my_array2.insert(4, 21)
my_array2.append(21)
print(my_array2.count(21))

# 2 Dimensional Array

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr1)
# inserting into a 2D array
arr2 = np.insert(arr1, 1, [[14, 15, 16, 17]], axis=0)
print(arr2)

arr3 = np.append(arr2, [[18, 19, 20, 21]], axis=0)
print(arr3)

# accessing elements in a 2d array
# a[i][j] i = row and j= column


def accessElements(arr, row, col):
    if row >= len(arr) and col >= len(arr[0]):  # -------------------O(1)
        print('Incorrect index provided')  # ------------------------O(1)
    else:
        print(arr[row][col])  # -------------------------------------O(1)


accessElements(arr3, 1, 2)

# Traversal


def traverseTwoDArray(array):
    for i in range(0, len(array)):  # --------------------O(n)
        for j in range(len(array[0])):  # ----------------O(mn)
            print(array[i][j])  # ------------------------O(1)


# time complexity will be O(n^2)
# Space Complexity = O(1)
traverseTwoDArray(arr3)

# Searching for an element in 2D array


def linearSearch2(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return f'FOUND!! The element is found at index : {i},{j}'
    return 'The element is not found'


print(linearSearch2(arr3, 50))
