import pytest
from maxCoins import Solution


@pytest.mark.parametrize("nums, expected", [
    ([3, 1, 5, 8], 167)
])
def test_maxCoins(nums, expected):
    actual = Solution().maxCoins(nums)
    assert actual == expected
