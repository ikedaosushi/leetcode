# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        middle = self._find_middle(head)
        right_head = middle.next
        middle.next = None
        return self._merge_sort(self.sortList(head), self.sortList(right_head))

    def _find_middle(self, head):
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def _merge_sort(self, left, right):
        head1, head2 = left, right
        head = ListNode(0)
        current = head
        while head1 and head2:
            if head1.val < head2.val:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next

        current.next = head1 or head2
        return head.next


if __name__ == "__main__":
    nums = [4, 2, 1, 3]
    head = ListNode(nums[0])
    current = head
    for x in nums[1:]:
        current.next = ListNode(x)
        current = current.next

    actual = Solution().sortList(head)
    while actual is not None:
        print(actual.val)
        actual = actual.next
