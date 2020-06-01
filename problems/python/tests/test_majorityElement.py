import pytest
from majorityElement import Solution


@pytest.mark.parametrize("nums,expected", [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([2], 2),
    ([2, 2], 2)
])
def test_majorityElement(nums, expected):
    actual = Solution().majorityElement(nums)
    assert actual == expected
