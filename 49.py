# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def groupAnagrams(strs):
    map = {}
    
    for i in range(len(strs)):
        letter_counts = [0] * 26
        for letter in strs[i]:
            index = ord(letter) - ord('a')
            letter_counts[index] += 1

        letter_counts = tuple(letter_counts)

        if letter_counts in map:
            map[letter_counts].append(strs[i])
        else:
            map[letter_counts] = [strs[i]]

    anagrams = []

    for key in map:
        anagrams.append(map[key])

    return anagrams

strs = ['abc', 'cba', 'bba', 'abb']

print(groupAnagrams(strs))