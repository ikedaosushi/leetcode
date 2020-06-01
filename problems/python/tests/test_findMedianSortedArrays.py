import pytest
from findMedianSortedArrays import Solution


@pytest.mark.parametrize("nums1, nums2, expected", [
    ([1, 3], [2], 2),
    ([1, 2], [3, 4], 2.5),
    ([1, 2], [3, 4, 5], 3.0)
])
def test_findMedianSortedArrays(nums1, nums2, expected):
    actual = Solution().findMedianSortedArrays(nums1, nums2)
    assert actual == expected
