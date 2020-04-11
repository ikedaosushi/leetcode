import pytest
from firstUniqChar import Solution


@pytest.mark.parametrize("s, expected", [
    ("leetcode", 0),
    ("loveleetcode", 2)
])
def test_firstUniqChar(s, expected):
    actual = Solution().firstUniqChar(s)
    assert actual == expected
