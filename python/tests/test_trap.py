import pytest
from trap import Solution


@pytest.mark.parametrize("height, expected", [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
])
def test_trap(height, expected):
    actual = Solution().trap(height)
    assert actual == expected
