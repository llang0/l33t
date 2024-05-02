# 229. Majority Element II

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.



def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # make a map of the counts of all numbers
    map = {}
    output = []
    for i in range(len(nums)):
        if nums[i] in map:
            map[nums[i]] += 1
        else:
            map[nums[i]] = 1
            
    for key in map:
        if map[key] > len(nums)/3:
            output.append(key)

    return output

nums = [3,2,3]

print(majorityElement(nums))