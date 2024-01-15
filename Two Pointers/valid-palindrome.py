# https://leetcode.com/problems/valid-palindrome/description/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Sol - 1 - O(n) time O(1) space
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1

        return True
    
# Sol 2 - O(n) space time 

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         filtered_chars = filter(lambda ch: ch.isalnum(), s)
#         lowered_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)
# 
#         lowered_filtered_chars_list = list(lowered_filtered_chars)
#         reversed_lowered_filtered_chars_list = lowered_filtered_chars_list[::-1]
# 
#         return lowered_filtered_chars_list == reversed_lowered_filtered_chars_list
