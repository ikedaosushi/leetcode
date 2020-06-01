import pytest
from partition import Solution


@pytest.mark.parametrize("s, expected", [
    ("aab", [["aa", "b"], ["a", "a", "b"]])
])
def test_partition(s, expected):
    actual = Solution().partition(s)
    assert sorted(actual) == sorted(expected)
