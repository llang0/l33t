# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    map = {}
    for i in range(len(nums)):
        if nums[i] in map:
            map[nums[i]] += 1
        else: 
            map[nums[i]] = 1

    for key in map:
        if map[key] > len(nums)/2:
            return key


nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))