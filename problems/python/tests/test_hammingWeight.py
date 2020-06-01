import pytest
from hammingWeight import Solution


@pytest.mark.parametrize("n, expected", [
    ("00000000000000000000000000001011", 3),
    ("00000000000000000000000010000000", 1),
])
def test_hammingWeight(n, expected):
    actual = Solution().hammingWeight(int(n))
    assert actual == expected
