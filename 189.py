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
    
def rotate2(nums, k):
    # step 1: reverse array
    l, r = 0, len(nums)-1
    while r > l:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    # step 2, reverse the first k items
    l, r = 0, k - 1
    while r > l:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    
    # step 3, reverse the last len-k items
    l, r = k, len(nums) -1
    while r > l:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1


nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)

nums = [1,2,3,4,5,6,7]
rotate2(nums, 3)
print(nums)

