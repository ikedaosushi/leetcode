import pytest
from reverseBits import Solution


@pytest.mark.parametrize("n, expected", [
    ("00000010100101000001111010011100", "00111001011110000010100101000000"),
    ("11111111111111111111111111111101", "10111111111111111111111111111111")
])
def test_reverseBits(n, expected):
    actual = Solution().reverseBits(int(n, 2))
    assert actual == int(expected, 2)
