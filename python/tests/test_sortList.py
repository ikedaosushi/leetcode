import pytest
from sortList import Solution


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


@pytest.mark.parametrize("nums,expected_nums", [
    ([4, 2, 1, 3], [1, 2, 3, 4]),
    ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
])
def test_sortList(nums, expected_nums):
    if len(nums) == 0:
        assert not Solution().sortList(None)
        return

    # prepare input
    head = ListNode(nums[0])
    current = head
    for x in nums[1:]:
        current.next = ListNode(x)
        current = current.next

    # prepare expected
    expected = ListNode(expected_nums[0])
    current = expected
    for x in expected_nums[1:]:
        current.next = ListNode(x)
        current = current.next

    actual = Solution().sortList(head)

    while actual is not None or expected is not None:
        assert actual.val == expected.val
        actual = actual.next
        expected = expected.next
