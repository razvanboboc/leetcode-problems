# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursive solution O(n + m) space time

class Solution:
    def mergeTwoLists(self, l1, l2):
        # define base cases for when a list has no nodes left
        # we just return the remainder of the other list
        if not l1:
            return l2
        elif not l2:
            return l1
        # compare heads, traverse the one with smaller value to compute next smaller values
        # by doing this, we will always get the smaller head at each recursive call
        # building a sorted new list
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            # return head
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            # return head
            return l2 
        
# Iterative Solution O(n + m) time, O(1) space
        
class Solution:
    def mergeTwoLists(self, l1, l2):
        # define preHead node 
        preHead = ListNode(-1)
        # define a prev pointer 
        prev = preHead
        # while there are still elements in l1 and l2 
        while l1 and l2:
            # if l1.val <= l2.val
            if l1.val <= l2.val:
                # add link from prev node to this
                prev.next = l1
                # shift l1 pointer to next element 
                l1 = l1.next
            # else
            else:
                # add link from prev node to this
                prev.next = l2
                # shift l2 pointer to next element 
                l2 = l2.next
            # shift prev node pointer
            prev = prev.next
        # prev.next = l1 or l2, depending which is not None
        prev.next = l1 or l2
        return preHead.next         