# 88. Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.



def merge(nums1, m, nums2, n):
    # m-1 is the index of the largest element in nums1
    # n-1 is the index of the largest element in nums2
    
    # if nums2 is empty don't do anything
    if n == 0: return

    # we are going to start counting backwards
    # so we need to get the last index of nums 1
    last = len(nums1) - 1

    # as long we're not already looking at the smallest number 
    # of either array
    while n > 0 and m > 0:
        # compare the two largest numbers
        if nums2[n-1] >= nums1[m-1]: # if nums2 has the bigger or equal number 
            nums1[last] = nums2[n-1]
            n -= 1 # move the pointer to the left
        else:
            nums1[last] = nums1[m-1]
            m -= 1
        last -= 1 # move the last pointer

    while n > 0:
        nums1[last] = nums2[n-1]
        n -= 1
        last -= 1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(f"final {nums1}")