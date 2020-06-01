import pytest
from longestSubstring import Solution


@pytest.mark.parametrize("s, k, expected", [
    ("aaabb", 3, 3),
    ("ababbc", 2, 5)
])
def test_longestSubstring(s, k, expected):
    actual = Solution().longestSubstring(s, k)
    assert actual == expected
