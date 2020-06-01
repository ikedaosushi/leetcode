import pytest
from plusOne import Solution


@pytest.mark.parametrize("digits,expected", [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([1], [2]),
    ([0], [1]),
])
def test_plusOne(digits, expected):
    actual = Solution().plusOne(digits)
    assert actual == expected
