# Built in Datastructure used to store a collection of items
# -They are ordered
# -They are mutable
# -Allow duplicates

integers = [1, 2, 3, 4]
print(integers)

stringList = ['Milk', 'Cheese', 'Butter']
print(stringList)

# Lists can store different data types

mixeList = [1, 'spam', 2.33]
print(mixeList)

nestedList = [1, 2, 4, 5, ['test', 'milky', 'way']]
print(nestedList)

empty = []
print(empty)

# Accessing/Traversing the List
shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[2])  # Access Butter

# in Operator

print('Milk' in shoppingList)  # Also Case Sensitive

print(shoppingList[-2])

# Traversing through the List
for i in shoppingList:
    print(i)

for j in range(len(shoppingList)):
    shoppingList[j] = shoppingList[j] + '+'
    print(shoppingList[j])

# Update item in a list
myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
myList[2] = 33
print(myList)

# Insertion at the [beginning,anyplace,end of list,list to the list]
myList.insert(0, 0)  # -----------------O(n)
print(myList)
myList.insert(4, 89)
print(myList)
myList.append(12)  # -------------------O(1)
print(myList)
list1 = [9, 8, 7, 6, 5]
myList.extend(list1)  # ----------------O(n)
print(myList)

# Slice and Slice Lists
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[:2])
myList[:2] = ['x', 'y']
print(myList)
# Deleting an element from the list
myList.pop(0)
print(myList)
myList.pop()  # -----------------------O(1)/O(n)
print(myList)
# Delete method
del myList[3]  # ----------------------O(n)
print(myList)

myList.remove('d')  # -----------------O(n)
print(myList)

# SEARCHING FOR AN ELEMENT IN A LIST
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# in operator for searching for an element in a list
target = 500
if target in my_list:  # -------------------------O(n)
    print(f'{target} is in the list')
else:
    print(f'{target} is not in the list')

# Linear Search


def linear_search(p_list, p_value):
    for i, value in enumerate(p_list):  # -------------------O(n)
        if value == p_value:  # -----------------------------O(1)
            return i  # -------------------------------------O(1)
    return f"{p_value} not found in {p_list}"


print(linear_search(my_list, 60))

a = [1, 2, 3]
b = [4, 5, 6]
c = a+b
print(c)
d = a*2
print(d)
# len returns the length of the list
# max returns the item with the highest value in the list
# min returns the item with the lowest value in the list
# sum returns the sum of all elements in the list

s_list = []
while True:
    inp = input("Enter a number :")
    if inp == 'done':
        break
    value = float(inp)
    s_list.append(value)
average = sum(s_list)/len(s_list)
print(f'Average is {average}')
# List Comprehension
