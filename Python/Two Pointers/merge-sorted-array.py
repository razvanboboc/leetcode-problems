# https://leetcode.com/problems/merge-sorted-array/

# Sol 1 - O(m + n) time, O(m) space

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m] 
        
        p1 = 0
        p2 = 0

        for p in range(n + m):
            if p1 >= m:
                nums1[p] = nums2[p2]
                p2 += 1
                continue
            if p2 >= n:
                nums1[p] = nums1_copy[p1]
                p1 += 1
                continue

            if nums1_copy[p1] <= nums2[p2]:
                nums1[p] = nums1_copy[p1] 
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

# Sol 2 - O(m + n) time, O(1) space

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1        
        for p in reversed(range(m + n)):
            if p1 < 0:
                nums1[p] = nums2[p2]
                p2 -= 1
                continue
            if p2 < 0:
                nums1[p] = nums1[p1]
                p1 -= 1
                continue
            if nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else: 
                nums1[p] = nums1[p1]
                p1 -= 1
