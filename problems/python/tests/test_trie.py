import pytest
from trie import Trie


@pytest.mark.parametrize("actions,args,expecteds", [
    (
        ["insert", "search", "search", "startsWith", "insert", "search"],
        [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
        [None, True, False, True, None, True],
    )
])
def test_trie(actions, args, expecteds):
    trie = Trie()
    actuals = []
    for action, arg, expected in zip(actions, args, expecteds):
        actual = getattr(trie, action)(*arg)
        actuals.append(actual)
    assert actuals == expecteds
