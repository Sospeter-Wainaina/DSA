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
