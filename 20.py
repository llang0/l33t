# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Pseudocode:
    # convert string to list of chars so we can use python array methods
    # if the stack is empty, pop an item from the front of the array into the back of stack. 

    # While we still have characters in s:
        # check to see if the item s[0] "closes" the item in the back of the stack 
            # if it closes: remove s[0] and pop the last element of the stack
            # no: add s[0] to the end of the stack

    # once s reaches length 0, is there anything left in the stack? 
        # yes: not valid
        # no: valid

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """        
    stack = []
    s = list(s)
    while len(s) > 0:
        char = s.pop(0)

        if len(stack) == 0:
            stack.append(char)
            continue

        if closes(char, stack[-1]):
            stack.pop()
        else: 
            stack.append(char)

    if len(stack) == 0:
        return True
    else:
        return False
    
def closes(c, s):
    if c == ')':
        if s == '(': 
            return True 
        else: 
            return False
    elif c == '}':
        if s == '{': 
            return True 
        else: 
            return False
    elif c == ']':
        if s == '[': 
            return True 
        else: 
            return False
    else:
        return False

 
# s = "{{{(([({})]))}}}" # valid
s = "{{{(([({})])}}}" # invalid

print(isValid(s))