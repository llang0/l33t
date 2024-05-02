# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.



def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    prefix = [1]*len(nums)
    postfix = [1]*len(nums)

    for i in range(len(nums)):
        if i == 0:
            prefix[i] = 1
        else:
            prefix[i] = prefix[i-1] * nums[i-1]

    for i in range(len(nums), 0, -1):
        if i == len(nums):
            postfix[i-1] = 1
        else: 
            postfix[i-1] = postfix[i] * nums[i]

    for i in range(len(nums)):
        postfix[i] = postfix[i] * prefix[i]

    return postfix

nums = [-1,1,0,-3,3]

print(productExceptSelf(nums))