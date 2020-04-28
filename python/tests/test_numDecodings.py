import pytest
from numDecodings import Solution


@pytest.mark.parametrize("s, expected", [
    ("12", 2),
    ("226", 3)
])
def test_numDecodings(s, expected):
    actual = Solution().numDecodings(s)
    assert actual == expected
