import pytest
from singleNumber import Solution


@pytest.mark.parametrize("nums, expected", [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
])
def test_singleNumber(nums, expected):
    actual = Solution().singleNumber(nums)
    assert actual == expected
