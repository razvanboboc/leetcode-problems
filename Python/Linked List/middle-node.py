# https://leetcode.com/problems/middle-of-the-linked-list/

# Sol 1 - O(n) space time

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head] 
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]

# Sol 2 - O(n) space O(1) time

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
        return slow