# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# this problem reminds me of the ransom problem

# make a dict of characters in s
# like this 
# {
#     a: 3
#     n: 1
#     g: 1
#     r: 1
# }

# if char[i] of t is in s
    # subtract 1 from dict[char[i]] 
# else
    # return false
# return true

# if you make it all the way through t but you still have letters left in the dict
# return false

def isAnagram(s, t):
    # make the dict
    dict = {}
    for char in s:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    
    # iterate through t while checking for chars in dict 
    for char in t:
        if not char in dict or dict[char] == 0:
            return False
        else: 
            dict[char] -= 1

    for char in dict:
        if not dict[char] == 0:
            return False
        
    return True

s = "ab"
t = "a"

print(isAnagram(s, t))
