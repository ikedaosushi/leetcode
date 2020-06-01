import pytest
from countSubstrings import Solution


@pytest.mark.parametrize("s, expected", [
    ("abc", 3),
    ("aaa", 6),
    ("fdsklf", 6)
])
def test_countSubstrings(s, expected):
    actual = Solution().countSubstrings(s)
    assert actual == expected
