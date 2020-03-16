import pytest
from findAnagrams import Solution


@pytest.mark.parametrize("s, p, expected", [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2])
])
def test_findAnagrams(s, p, expected):
    actual = Solution().findAnagrams(s, p)
    assert actual == expected
