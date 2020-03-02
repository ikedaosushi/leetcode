import pytest
from countBits import Solution


@pytest.mark.parametrize("num, expected", [
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2])
])
def test_countBits(num, expected):
    actual = Solution().countBits(num)
    assert actual == expected
