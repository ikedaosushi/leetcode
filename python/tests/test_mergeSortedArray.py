import pytest
from mergeSortedArray import Solution


@pytest.mark.parametrize("nums1,m,nums2,n,expected", [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([3, 5, 0, 0, 0], 2, [1, 2, 6], 3, [1, 2, 3, 5, 6]),
    ([3, 5, 0, 0, 0, 0, 0], 2, [1, 2, 6, 7, 8], 5, [1, 2, 3, 5, 6, 7, 8]),
])
def test_mergeSortedArray(nums1, m, nums2, n, expected):
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == expected
