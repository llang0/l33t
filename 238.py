# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):
    output = [1]*len(nums)

    prefix = 1
    for i in range(len(nums)):
        if i != 0:
            prefix = prefix * nums[i-1]
        output[i] = prefix

    postfix = 1
    for i in range(len(nums), 0, -1):
        if i != len(nums):
            postfix = postfix * nums[i]
            output[i-1] = output[i-1] * postfix

    return output

nums = [1, 2, 3, 4]

print(productExceptSelf(nums))