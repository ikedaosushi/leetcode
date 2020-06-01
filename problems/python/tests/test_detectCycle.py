import pytest
from detectCycle import Solution


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


@pytest.mark.parametrize("nums,pos,expected", [
    ([], -1, None),
    ([1], -1, None),
    ([1, 2], 0, 0),
    ([3, 2, 0, -4], 1, 1)
])
def test_detectCycle(nums, pos, expected):
    if len(nums) == 0:
        assert not Solution().detectCycle(None)
        return

    # prepare input
    head = ListNode(nums[0])
    idx = 0
    tail = None
    current = head
    for x in nums[1:]:
        current.next = ListNode(x)
        if idx == pos:
            tail = current
        current = current.next
        idx += 1
    current.next = tail

    expected = tail
    actual = Solution().detectCycle(head)

    assert actual == expected
