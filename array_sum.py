# find numbers whose sum is equal to a given number
# [2,6,3,9,11] 9----> [6,3]

# in an interview ask the correct answers e.g
# #Does the array contain only positive numbers?
# Are reverse pairs accepted e.g (1,4) is it the same as (4,1)
# Should we only print distinct pairs?

def find_pairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)


#find_pairs([1, 2, 3, 3, 4, 5], 6)

def two_sum(nums, targ):
    seen = {}
    for i, num in enumerate(nums):
        complement = targ-num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


two_sum([1, 2, 3, 3, 4, 5], 6)
