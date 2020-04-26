import pytest
from reverseString import Solution


@pytest.mark.parametrize("s, expected", [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
])
def test_reverseString(s, expected):
    Solution().reverseString(s)
    assert s == expected
