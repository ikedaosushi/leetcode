import pytest
from findTargetSumWays import Solution


@pytest.mark.parametrize("nums, S, expected", [
    ([1, 1, 1, 1, 1], 3, 5)
])
def test_findTargetSumWays(nums, S, expected):
    actual = Solution().findTargetSumWays(nums, S)
    assert actual == expected
