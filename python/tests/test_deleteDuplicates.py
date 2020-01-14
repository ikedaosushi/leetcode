import pytest
from deleteDuplicates import Solution


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


@pytest.mark.parametrize("nums,expected_nums", [
    ([], []),
    ([1], [1]),
    ([1, 1, 2], [1, 2]),
    ([1, 1, 2, 3, 3], [1, 2, 3])
])
def test_deleteDuplicates(nums, expected_nums):
    if len(nums) == 0:
        assert Solution().deleteDuplicates(None) is None
        return

    # prepare input
    head = ListNode(nums[0])
    if len(nums) > 1:
        current = head
        for x in nums[1:]:
            current.next = ListNode(x)
            current = current.next

    # prepare expected
    expected = ListNode(expected_nums[0])
    if len(expected_nums) > 1:
        current = expected
        for x in expected_nums[1:]:
            current.next = ListNode(x)
            current = current.next

    actual = Solution().deleteDuplicates(head)

    while actual is not None or expected is not None:
        assert actual.val == expected.val
        actual = actual.next
        expected = expected.next
