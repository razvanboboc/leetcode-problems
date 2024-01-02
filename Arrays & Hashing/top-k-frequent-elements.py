# https://leetcode.com/problems/top-k-frequent-elements/description/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Sol 1 - Brute force 

# Sol 2 - Min-Heap - O(Nlogk) time complexity, O(n+k) space complexity

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        occurences = {}
        for i in nums:
            occurences[i] = occurences.get(i, 0) + 1
        heap = [] 
        for i in occurences:
            if len(heap) == k:
                heappushpop(heap, [occurences[i], i])
            else:
                heappush(heap, [occurences[i], i])
        ans = []
        while k > 0: 
            k -= 1
            ans.append(heappop(heap)[1])
        return ans

# Sol 3 - Hash map with buckets O(N) time complexity, O(N) space complexity
    
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freqTable = {}
#         for i in nums:
#             freqTable[i] = 1 + freqTable.get(i, 0)
#         bucketArr = [[] for i in range(len(nums))]
#         for i in freqTable:
#             bucketArr[freqTable[i] - 1].append(i)
#         ans = []
#         for i in range(len(nums), 0, -1):
#             if len(bucketArr[i - 1]) != 0 and k != 0:
#                 for j in range(0, len(bucketArr[i - 1])):
#                     ans.append(bucketArr[i - 1][j])
#                     k -= 1
#                     if(k == 0): 
#                         break
#         return ans

