
def remove_duplicates(arr):
    seen = []
    for i in arr:
        if i in seen:
            continue
        else:
            seen.append(i)
    return seen


remove_duplicates([1, 1, 2, 2, 3, 4, 5])


def remove_duplicates2(arr):
    return set(arr)


print(remove_duplicates2([1, 1, 2, 2, 3, 4, 5]))
