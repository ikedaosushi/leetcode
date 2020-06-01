import pytest
from coinChange import Solution


@pytest.mark.parametrize("coins, amount, expected", [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([2147483647], 2, -1)
])
def test_coinChange(coins, amount, expected):
    actual = Solution().coinChange(coins, amount)
    assert actual == expected
