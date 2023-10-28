def rotate_matrix(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for row in arr:
        row.reverse()
    return arr


print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
