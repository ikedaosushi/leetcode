import pytest
from productExceptSelf import Solution


@pytest.mark.parametrize("nums,expected", [
    ([1, 2], [2, 1]),
    ([1, 2, 3, 4], [24, 12, 8, 6])
])
def test_productExceptSelf(nums, expected):
    actual = Solution().productExceptSelf(nums)
    assert actual == expected
