import pytest
from maxProfitSimple import Solution


@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0)
])
def test_maxProfit(prices, expected):
    actual = Solution().maxProfit(prices)
    assert actual == expected
