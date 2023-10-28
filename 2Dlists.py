# find the sum of diagonal values in a 2d List
myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def diagonal_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i][i]
    print(total)


diagonal_sum(myList2D)
