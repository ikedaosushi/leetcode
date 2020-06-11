import pytest
from strStr import Solution


@pytest.mark.parametrize("haystack, needole, expected", [
    ("hello", "ll", 2),
    ("aaaaa", "bba", -1),
    ("aaaaaaa", "aaa", 0),
    ("", "", 0)
])
def test_strStr(haystack, needole, expected):
    actual = Solution().strStr(haystack, needole)
    assert actual == expected
