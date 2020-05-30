class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while True:
            if not fast.next:
                return slow
            elif not fast.next.next:
                return slow.next
            else:
                slow = slow.next
                fast = fast.next.next
