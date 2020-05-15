import pytest
from calculate import Solution


@pytest.mark.parametrize("s, expected", [
    ("3+2*2", 7),
    ("3-2*2", -1),
    ("3/2", 1),
    ("3+5 / 2", 5),
    ("3+2*2", 7)
])
def test_calculate(s, expected):
    actual = Solution().calculate(s)
    assert actual == expected
