# https://leetcode.com/problems/design-linked-list/

# Solution using single list
# Time complexity: O(1) for addAtHead. O(k) for get, addAtIndex, and deleteAtIndex, where kkk is an index of the element to get, add or delete. O(N) for addAtTail.
# Space complexity: O(1) for all operations.\

class ListNode: 
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        target = self.head
        for _ in range(index + 1):
            target = target.next
        return target.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index < 0:
            index = 0
        
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        newNode = ListNode(val)
        newNode.next = pred.next
        pred.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        self.size -= 1 
        pred = self.head
        
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
