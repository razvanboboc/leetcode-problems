# https://leetcode.com/problems/top-k-frequent-elements/description/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Sol 1 - Brute force 

# Sol 2 - Min-Heap 

# Sol 3 - Min-Heap Optimised

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
        # create a heap 
        # iterate hashmap 
            # if len(heap) > k
                # heappushpop current element 
            # elif 
                # heappush current element
        # initiate array for answer 
            # iterate heap and push current element 
        # return answer array
