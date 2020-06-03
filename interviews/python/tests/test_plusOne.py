import pytest
from plusOne import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], [1, 2, 4]),
    ([9], [1, 0]),
    ([4, 3, 2, 1], [4, 3, 2, 2])
])
def test_plusOne(nums, expected):
    actual = Solution().plusOne(nums)
    assert actual == expected
