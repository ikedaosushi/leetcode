import pytest
from canCompleteCircuit import Solution


@pytest.mark.parametrize("gas, cost, expected", [
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ([2, 3, 4], [3, 4, 3], -1)
])
def test_canCompleteCircuit(gas, cost, expected):
    actual = Solution().canCompleteCircuit(gas, cost)
    assert actual == expected
