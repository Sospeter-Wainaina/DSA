# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]
def middle(lst):
    lst.pop()
    lst.remove(lst[0])
    print(lst)


# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]

def middle_values(list_p):
    return list_p[1:-1]


middle_values([1, 2, 3, 4])
