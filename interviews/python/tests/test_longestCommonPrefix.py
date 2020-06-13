import pytest
from longestCommonPrefix import Solution


@pytest.mark.parametrize("strs, expected", [
    ([], ""),
    (["", ""], ""),
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], "")
])
def test_longestCommonPrefix(strs, expected):
    actual = Solution().longestCommonPrefix(strs)
    assert actual == expected
