# https://leetcode.com/problems/two-sum/description/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Sol 1 - O(n2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
# Sol 2 - O(n)
                
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(nums)): 
#             hashmap[nums[i]] = i
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap and hashmap[complement] != i:
#                 return [i, hashmap[complement]]

# Sol 3 - O(n) - one way pass 

#  class Solution:
#      def twoSum(self, nums: List[int], target: int) -> List[int]:
#          hashmap = {}
#          for i in range(len(nums)):
#              complement = target - nums[i]
#              if complement in hashmap and hashmap[complement] != i:
#                  return [i, hashmap[complement]]
#              hashmap[nums[i]] = i                