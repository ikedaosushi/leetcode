import pytest
from minWindow import Solution


@pytest.mark.parametrize("s, t, expected", [
    ("ADOBECODEBANC", "ABC", "BANC")
])
def test_minWindow(s, t, expected):
    actual = Solution().minWindow(s, t)
    assert actual == expected
