# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.


def first_second(my_list):
    best1, best2 = 0, 0
    for i in my_list:
        if i > best1:
            best2 = best1
            best1 = i
        elif i > best2 and i < best1:
            best2 = i
    return best1, best2


myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(myList))
