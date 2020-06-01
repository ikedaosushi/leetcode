import pytest
from wiggleSort import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1, 5, 1, 1, 6, 4], [1, 6, 1, 5, 1, 4]),
    ([1, 3, 2, 2, 3, 1], [2, 3, 1, 3, 1, 2]),
    ([1, 1, 2, 1, 2, 2, 1], [1, 2, 1, 2, 1, 2, 1])
])
def test_wiggleSort(nums, expected):
    Solution().wiggleSort(nums)
    assert nums == expected
