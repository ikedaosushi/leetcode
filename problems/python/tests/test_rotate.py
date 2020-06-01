import pytest
from rotate import Solution


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100])
])
def test_rotate(nums, k, expected):
    Solution().rotate(nums, k)
    assert nums == expected
