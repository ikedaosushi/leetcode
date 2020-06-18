class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast == fast.next.next

        return False
