import pytest
from leastInterval import Solution


@pytest.mark.parametrize("tasks, n, expected", [
    # ([], 2, 0),
    (["A", "B"], 0, 2),
    (["A", "A", "A", "B", "B", "B"], 2, 8),
    (["A", "A", "A", "B", "B", "B"], 0, 6),
    ([
        "A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F", "G", "G", "H", "H", "I", "I", "J", "J", "K", "K",
        "L", "L", "M", "M", "N", "N", "O", "O", "P", "P", "Q", "Q", "R", "R", "S", "S", "T", "T", "U", "U", "V", "V",
        "W", "W", "X", "X", "Y", "Y", "Z", "Z"
    ], 2, 52)
])
def test_leastInterval(tasks, n, expected):
    actual = Solution().leastInterval(tasks, n)
    assert actual == expected
