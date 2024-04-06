# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

# Sol 1 using stacks - O(n) space time complexity

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["$", 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * count for c, count in stack)

# Sol 2 using string / sets
    
# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         setChars = set(s)
#         removeArray = [c * k for c in setChars]
#         while True:
#             starter = s
#             for duplicate in removeArray:
#                 if duplicate in s:
#                     s = s.replace(duplicate, '')
#             if starter == s:
#                 return s
