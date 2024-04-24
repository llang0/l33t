# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# I already know that checking each number against every other number would give
# a solution with time complexity of O(n^2)

# but maybe I can do better if I make a dict like this

# nums = [2,7,11,15]
# dict = {
#     2: [0],
#     7: [1],
#     11: [2],
#     15: [3]
# }

# I need to keep in mind the same number can appear more than once, but you can only use it once

# nums = [3, 3]
# dict = {3: [0, 1]}

# In that case i need to consume one of the threes by popping it off the array

def twoSum(nums, target):
    # make the dict
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict:
            dict[nums[i]].append(i)
        else:
            dict[nums[i]] = [i]

    # now we can lookup the remainder in the dict
    for i in range(len(nums)):
        temp = dict[nums[i]].pop(0) # pop the index of i off the dict so we don't reference the same num twice
        remainder = target-nums[i]
        if remainder in dict and len(dict[remainder]) != 0:
            return [temp, dict[remainder][0]]
        
nums = [-1,-2,-3,-4,-5]
target = -8
print(twoSum(nums, target))


