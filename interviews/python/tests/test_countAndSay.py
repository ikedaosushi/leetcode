import pytest
from countAndSay import Solution


@pytest.mark.parametrize("n, expected", [
    (1, "1"), (4, "1211")
])
def test_countAndSay(n, expected):
    actual = Solution().countAndSay(n)
    assert actual == expected
