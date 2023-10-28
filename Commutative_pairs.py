def pair_sum(arr, n):
    pairs = []
    seen = set()
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            element1 = arr[i]
            element2 = arr[j]
            current_pair = (element1, element2)
            if element1+element2 == n:
                if current_pair not in seen and (element2, element1) not in seen:
                    pairs.append(current_pair)
                    seen.add(current_pair)
    return pairs


result1 = pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)
print(result1)


def pair_sum2(arr, n):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == n:
                result.append(f"{arr[i]} + {arr[j]}")

    return result


result = pair_sum2([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)
print(result)
