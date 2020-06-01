import pytest
from isHappy import Solution


@pytest.mark.parametrize("n, expected", [
    (19, True)
])
def test_isHappy(n, expected):
    actual = Solution().isHappy(n)
    assert actual == expected
