import pytest
from numIslands import Solution


@pytest.mark.parametrize("nums,expected", [
    ([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ], 1),
    ([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["1", "0", "1", "1", "0"],
        ["0", "0", "0", "1", "1"]
    ], 2),
    ([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["1", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ], 3),
])
def test_numIslands(nums, expected):
    actual = Solution().numIslands(nums)
    assert actual == expected
