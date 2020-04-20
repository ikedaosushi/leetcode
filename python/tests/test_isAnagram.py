import pytest
from isAnagram import Solution


@pytest.mark.parametrize("s, t, expected", [
    ("", "", True),
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("aacc", "ccac", False),
    ("ab", "a", False),
    ("aa", "a", False)
])
def test_isAnagram(s, t, expected):
    actual = Solution().isAnagram(s, t)
    assert actual == expected
