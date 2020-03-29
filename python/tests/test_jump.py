import pytest
from jump import Solution


@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], 2),
    ([1, 2, 3], 2)
])
def test_jump(nums, expected):
    actual = Solution().jump(nums)
    assert actual == expected
