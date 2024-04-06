# https://leetcode.com/problems/valid-anagram/description/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Sol 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        
        return True

## Sol 2 - using hash set, n time complexity
    
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
# 
#         charCount = set(s)
#         for char in charCount:
#             if s.count(char) != t.count(char):
#                 return False 
#         return True
    

## Sol 3 - Using sort n log n Complexity
    
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         sortedS = ''.join(sorted(s))
#         sortedT = ''.join(sorted(t))
#         
#         if sortedS == sortedT:
#             return True
#         return False
    
## Sol 4 - Table counter, O(n) time complexity, table accessing is fast
    
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         tableCounter = [0] * 26
#         for char in s:
#             tableCounter[ord(char) - ord('a')] += 1
#         for char in t: 
#             tableCounter[ord(char) - ord('a')] -= 1
#             if tableCounter[ord(char) - ord('a')] < 0:
#                 return False 
#         return True