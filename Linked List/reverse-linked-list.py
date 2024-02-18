# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative Sol - O(n) time, O(1) space

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init prev pointer 
        previous = None
        # init current node pointer 
        current = head
        # while there are still nodes in list 
        while current:
            # save instance of next node
            nextNode = current.next
            # make current node point to previous 
            current.next = previous
            # shift prev pointer to current node
            previous = current
            # shift current pointer to next node in list
            current = nextNode
        # return head
        return previous