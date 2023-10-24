def missing_number(arr, n):
    init = n*(n+1)//2
    arr_sum = sum(arr)
    miss_number = init-arr_sum
    return miss_number


print(missing_number([1, 2, 3, 5, 6], 6))  # 4
