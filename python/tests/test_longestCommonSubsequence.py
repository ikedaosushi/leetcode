import pytest
from longestCommonSubsequence import Solution


@pytest.mark.parametrize("text1, text2, expected", [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0)
])
def test_longestCommonSubsequence(text1, text2, expected):
    actual = Solution().longestCommonSubsequence(text1, text2)
    assert actual == expected
