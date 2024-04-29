# 26. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    map = {}

    for i in range(len(nums)):
        if nums[i] in map:
            map[nums[i]].append(i)
        else:
            map[nums[i]] = [i]


    for val in map:
        while len(map[val]) > 1:
            idx = map[val].pop()
            nums[idx] = None

    i = len(nums)-1
    while i >= 0:
        if nums[i] == None:
            nums.pop(i)
        
        i -= 1

    return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))
print(nums)