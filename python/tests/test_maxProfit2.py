import pytest
from maxProfit2 import Solution


@pytest.mark.parametrize("nums, expected", [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0)
])
def test_maxProfit(nums, expected):
    actual = Solution().maxProfit(nums)
    assert actual == expected
