import pytest
from maxProfit import Solution


@pytest.mark.parametrize("nums,expected", [
    ([1, 2, 3, 0, 2], 3)
])
def test_maxProfit(nums, expected):
    actual = Solution().maxProfit(nums)
    assert actual == expected
