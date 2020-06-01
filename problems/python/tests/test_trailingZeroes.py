import pytest
from trailingZeroes import Solution


@pytest.mark.parametrize("n, expected", [
    (3, 0),
    (5, 1)
])
def test_trailingZeroes(n, expected):
    actual = Solution().trailingZeroes(n)
    assert actual == expected
