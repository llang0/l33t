# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    first = 0
    last = len(s)-1

    while last > first: 
        if not isAlphanum(s[first]):
            first += 1
        elif not isAlphanum(s[last]):
            last -= 1
        elif s[first].lower() == s[last].lower():
            first += 1
            last -= 1
        else:
            return False
    return True

def isAlphanum(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return True
    elif ord(c) >= ord('0') and ord(c) <= ord('9'):
        return True
    else:
        return False

s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))