class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current

        return prev


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    head = ListNode(nums[0])
    current = head
    for x in nums[1:]:
        current.next = ListNode(x)
        current = current.next

    nums.reverse()
    expected = ListNode(nums[0])
    current = expected
    for x in nums[1:]:
        current.next = ListNode(x)
        current = current.next

    actual = Solution().reverseList(head)

    while actual or expected:
        print("a:", actual.val, "e:", expected.val)
        actual = actual.next
        expected = expected.next
