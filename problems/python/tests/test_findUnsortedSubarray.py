import pytest
from findUnsortedSubarray import Solution

@pytest.mark.parametrize("nums, expected", [
    ([2, 6, 4, 8, 10, 9, 15], 5),
    ([1,2,3,4], 0)
])
def test_findUnsortedSubarray(nums, expected):
    actual = Solution().findUnsortedSubarray(nums)
    assert actual == expected
