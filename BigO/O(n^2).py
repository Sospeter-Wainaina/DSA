#BigO (n^2)
boxes = ['a', 'b', 'c', 'd', 'e']

def logAllPairsOfArray(array):
    for i in array:
        for j in array:
            print(i, j)
logAllPairsOfArray(boxes)

#nested loops we `multiply` the two loops O(n^2)
#Quadratic Time 

#Rule 4: Drop Non Dominants

def printAllNumbersThenAllPairSums(numbers):
    print('these are the numbers:')
    for number in numbers:
        print(number)

    print('and these are their sums:')
    for firstNumber in numbers:
        for secondNumber in numbers:
            print(firstNumber + secondNumber)

printAllNumbersThenAllPairSums([1, 2, 3, 4, 5])
# we drop the non dominants
# O(n + n^2) = O(n^2)