# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Sol 1 - Hash Map

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for i in range(len(nums)):
            if nums[i] in countMap and countMap[nums[i]] > 0:
                return True
            countMap[nums[i]] = countMap.get(nums[i], 0) + 1
        return False

## Sol 2 - Hash Set

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set() 
#         for num in nums: 
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False

## Sol 3 - Sort Array

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         n = len(nums)
#         for i in range(n - 1):
#             if nums[i] == nums[i + 1]:
#                 return True
#         return False