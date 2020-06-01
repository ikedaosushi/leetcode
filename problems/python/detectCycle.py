class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        is_cycled = False
        current = head
        while current:
            if current.val is None:
                is_cycled = True
                break
            current.val = None
            current = current.next

        res = current if is_cycled else None

        return res


if __name__ == "__main__":
    # nums, pos, expected = [3, 2, 0, -4], 1, 1
    nums, pos, expected = [1, 2], 0, 0

    head = ListNode(nums[0])
    current = head
    idx = 0
    tail = None
    for x in nums[1:]:
        current.next = ListNode(x)
        if idx == pos:
            tail = current
        current = current.next
        idx += 1
    current.next = tail

    actual = Solution().hasCycle(head)
    print("actual:", actual)
