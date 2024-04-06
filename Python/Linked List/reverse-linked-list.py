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

# Recursive Sol - O(n) time space
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # define base case 
        # if no current head or no existing next head 
        if (not head) or (not head.next):
            # return head 
            return head
        # init reference to last node by recursive call 
        lastNode = self.reverseList(head.next)
        # add link from next node to current node 
        head.next.next = head
        # delete link from current node 
        head.next = None
        # return reference to new head of reversed list
        return lastNode