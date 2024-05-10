# 189. Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    newArray = [0]*len(nums)
    
    for i in range(len(nums)):
        newArray[(i+k)%len(nums)] = nums[i]

    for i in range(len(nums)):
        nums[i] = newArray[i]
    
nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)