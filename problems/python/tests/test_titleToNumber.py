import pytest
from titleToNumber import Solution


@pytest.mark.parametrize("s, expected", [
    ("A", 1),
    ("AB", 28),
    ("ZY", 701),
])
def test_titleToNumber(s, expected):
    actual = Solution().titleToNumber(s)
    assert actual == expected
