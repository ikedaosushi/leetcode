import pytest
from topKFrequent import Solution


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
])
def test_topKFrequent(nums, k, expected):
    actual = Solution().topKFrequent(nums, k)
    assert actual == expected
