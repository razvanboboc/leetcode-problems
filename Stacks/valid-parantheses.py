# https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Sol 1 - O(n) space time

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in mappings:
                if stack and stack[-1] == mappings[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        
        return not stack