import pytest
from isPalindrome2 import Solution


@pytest.mark.parametrize("s, expected", [
    ("", True),
    (" ", True),
    ("0P", False),
    ("aa", True),
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False)
])
def test_isPalindrome2(s, expected):
    actual = Solution().isPalindrome(s)
    assert actual == expected
