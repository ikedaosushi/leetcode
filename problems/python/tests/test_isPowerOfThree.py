import pytest
from isPowerOfThree import Solution


@pytest.mark.parametrize("n, expected", [
    (27, True),
    (0, False),
    (9, True),
    (45, False)
])
def test_isPowerOfThree(n, expected):
    actual = Solution().isPowerOfThree(n)
    assert actual == expected
