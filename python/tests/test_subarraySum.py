import pytest
from subarraySum import Solution


@pytest.mark.parametrize("nums, k, expected", [
    ([], 2, 0),
    ([1, 1, 1], 2, 2),
    ([1, 1, 1, 1], 2, 3)
])
def test_subarraySum(nums, k, expected):
    actual = Solution().subarraySum(nums, k)
    assert actual == expected
