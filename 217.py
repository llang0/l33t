# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# tricky version: use python if _ in _ to test 
# for every element of the array 
# store that element to x
# set that element to None
# if x in array: if true then retun true
# if you get to the end of the array, return false

# this exceeds the time limit if nums is really big

# def containsDuplicate(nums):
#     x = None
#     for i in range(len(nums)):
#         x = nums[i]
#         nums[i] = None
#         if x in nums:
#             return True
        
#     return False


# this is faster, but not fast enough

# def containsDuplicate(nums):
#     x = None
#     # start at the end
#     i = len(nums) - 1
#     while i > 0:
#         x = nums[i]
#         nums.pop(i)
#         i -= 1
#         if x in nums: return True
#     return False


# make an array called seen.
# If num is not in seen, add it to the array then keep going
# if is in seen, return true
# if you get to the end of the loop return false

# def containsDuplicate(nums):
#     seen = []
#     for num in nums:
#         if not num in seen:
#             seen.append(num)
#         else: 
#             return True
#     return False

# nums = [1,2,3,4]

# experimental approach
# cut the array into smaller pieces of size two
# do any pieces contain repeats? 
    # if yes: return true
# if no: add every two peices together
    # check again: 

# this doesn't work but points for trying
# I almost solved it with a merge sort but I missed 🤦

# def slice(nums):
#     start = 0
#     end = len(nums)
#     step =2
#     new_list = []
#     for i in range(start, end, step):
#         x = i
#         new_list.append(nums[x:x+step])
#     return new_list

# def glue(slices):
#     start = 0
#     end = len(slices)
#     step = 2
#     new_list = []
#     for i in range(start, end, step):
#         chunck = []
#         for j in range(step):
#             for item in slices[i+j]:
#                 chunck.append(item)
#         new_list.append(chunck)
#         chunck = []
    
#     return new_list
            
# def containsDuplicate(nums):
#     # slice the main list into chunks of size 2
#     slices = slice(nums)
#     while len(slices) > 1:
#         seen = []
#         for chunck in slices:
#             if len(chunck) == 1: continue
#             for i in range(len(chunck)):
#                 if chunck[i] in seen:
#                     return True
#                 else: 
#                     seen.append(chunck[i])
#             seen = []
#         # if we get through everything and haven't returned
#         # glue the slices together and go again
#         slices = glue(slices)

#     # if you get all the way back to the original array: 
#     # you're screwed
#     x = None
#     # start at the end
#     i = len(nums) - 1
#     while i > 0:
#         x = nums[i]
#         nums.pop(i)
#         i -= 1
#         if x in nums: return True
#     return False

# using a hash set will give us instant lookup time on the seen array, so we can do 
# solution 3, but much faster

def containsDuplicate(nums):
    hashset = set()
    
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

nums = [1,2,3,4,1,2,3,4]

print(containsDuplicate(nums))

# TODO: create a solution that implements a merge sort