# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        if head.next == None:
            return head

        pointer = head
        length = 1

        while pointer.next:
            pointer = pointer.next
            length += 1

        rotateTimes = k % length

        if k == 0 or rotateTimes == 0:
            return head

        fastPointer = head
        slowPointer = head

        for a in range(rotateTimes):
            fastPointer = fastPointer.next

        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next

        tmp = slowPointer.next

        slowPointer.next = None
        fastPointer.next = head
        head = tmp

        return head
