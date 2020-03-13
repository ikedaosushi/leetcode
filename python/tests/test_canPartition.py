import pytest
from canPartition import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),
    ([23, 13, 11, 7, 6, 5, 5], True)
])
def test_canPartition(nums, expected):
    actual = Solution().canPartition(nums)
    assert actual == expected
