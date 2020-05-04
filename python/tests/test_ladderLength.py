import pytest
from ladderLength import Solution


@pytest.mark.parametrize("b, e, wl, expected", [
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ("hit", "cog", ["hot", "dot", "tog", "cog"], 0)
])
def test_ladderLength(b, e, wl, expected):
    actual = Solution().ladderLength(b, e, wl)
    assert actual == expected
