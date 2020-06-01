import pytest
from mergeKLists import Solution, ListNode


@pytest.mark.parametrize("nums_lists, expected", [
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])
])
def test_mergeKLists(nums_lists, expected):
    lists = []
    for nums in nums_lists:
        current = root = ListNode(nums[0])
        for n in nums[1:]:
            current.next = ListNode(n)
            current = current.next
        lists.append(root)

    actual = Solution().mergeKLists(lists)

    idx = 0
    while actual:
        assert actual.val == expected[idx]
        actual = actual.next
        idx += 1


def test_mergeKLists_if_null():
    assert Solution().mergeKLists([None]) is None
    assert Solution().mergeKLists([None, None]) is None
    assert Solution().mergeKLists([]) is None
    assert Solution().mergeKLists([None, ListNode(1)]).val == 1
