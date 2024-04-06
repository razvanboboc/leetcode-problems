# https://leetcode.com/problems/group-anagrams/description/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Sol 1 -  O(NK log K) time complexity

class Solution:
    def groupAnagrams(self, strs): 
        dictOfAnagrams = collections.defaultdict(list)
        for s in strs:
            sortedString = sorted(s)
            dictOfAnagrams[tuple(sortedString)].append(s)
        return dictOfAnagrams.values()
    
# Sol 2 - O(NK) time complexity
    

# class Solution:
#     def groupAnagrams(self, strs): 
#         dictOfAnagrams = collections.defaultdict(list)
#         for s in strs:
#             charOccurences = [0] * 26
#             for char in s:
#                 charOccurences[ord(char) - ord('a')] += 1
#             dictOfAnagrams[tuple(charOccurences)].append(s)
#         return dictOfAnagrams.values()