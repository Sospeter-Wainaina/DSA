#BigO (n^2)
boxes = ['a', 'b', 'c', 'd', 'e']

def logAllPairsOfArray(array):
    for i in array:
        for j in array:
            print(i, j)
logAllPairsOfArray(boxes)

#nested loops we `multiply` the two loops O(n^2)
#Quadratic Time 