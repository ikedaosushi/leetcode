import pytest
from lengthOfLIS import Solution


@pytest.mark.parametrize("nums,expected", [
    ([], 0),
    ([1], 1),
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([10, 9, 2, 5, 3, 7, 101, 180, 1], 5),
])
def test_lengthOfLIS(nums, expected):
    actual = Solution().lengthOfLIS(nums)
    assert actual == expected
