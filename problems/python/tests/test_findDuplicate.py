import pytest
from findDuplicate import Solution


@pytest.mark.parametrize("nums,expected", [
    ([1, 3, 4, 2, 2], 2),
    ([3, 1, 3, 4, 2], 3)
])
def test_findDuplicate(nums, expected):
    actual = Solution().findDuplicate(nums)
    assert actual == expected
