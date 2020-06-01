import pytest
from houseRobber import Solution


@pytest.mark.parametrize("nums,expected", [
    ([], 0),
    ([1], 1),
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
])
def test_houseRobber(nums, expected):
    actual = Solution().rob(nums)
    assert actual == expected
