class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        ca = headA
        cb = headB

        while ca is not cb:
            # print("ca:", ca.val, "cb:", cb.val)
            ca = ca.next if ca else headB
            cb = cb.next if cb else headA

        return ca


if __name__ == "__main__":
    # nums_a, nums_b, nums_a_idx, nums_b_idx = [4, 1, 8, 4, 5], [5, 0, 1, 8, 4, 5], 2, 3
    nums_a, nums_b, nums_a_idx, nums_b_idx = [4, 1, 8, 4, 5], [5, 0, 1, 8, 5, 5], None, None
    if not nums_a or not nums_b:
        assert Solution().getIntersectionNode(None, None) is None

    none_flag = nums_a_idx is None and nums_b_idx is None
    if none_flag:
        nums_a_idx = len(nums_a) + 1
        nums_b_idx = len(nums_b) + 1

    current_a = head_a = ListNode(nums_a[0])
    for x in nums_a[1:nums_a_idx]:
        current_a.next = ListNode(x)
        current_a = current_a.next

    current_b = head_b = ListNode(nums_b[0])
    for x in nums_b[1:nums_b_idx]:
        current_b.next = ListNode(x)
        current_b = current_b.next

    if not none_flag:
        current = expected = ListNode(nums_a[nums_a_idx])
        current_a.next = current
        current_b.next = current

        for x in nums_a[nums_a_idx + 1:]:
            current.next = ListNode(x)
            current = current.next

    actual = Solution().getIntersectionNode(head_a, head_b)

    if none_flag:
        assert actual is None
    else:
        while actual is not None or expected is not None:
            print("actual:", actual.val, "expected:", expected.val)
            assert actual.val == expected.val
            actual = actual.next
            expected = expected.next
