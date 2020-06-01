import pytest
from maxProduct import Solution


@pytest.mark.parametrize("nums,expected", [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([2, 3, -2, 4, 5, 8], 160),
    ([-4, -3, -2], 12)
])
def test_maxProduct(nums, expected):
    actual = Solution().maxProduct(nums)
    assert actual == expected
