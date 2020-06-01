import pytest
from findKthLargest import Solution


@pytest.mark.parametrize("nums,k,expected", [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)
])
def test_findKthLargest(nums, k, expected):
    actual = Solution().findKthLargest(nums, k)
    assert actual == expected
