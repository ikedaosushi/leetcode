import pytest
from minStack import MinStack


@pytest.mark.parametrize("actions,args,expecteds", [
    (
        ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
        [[], [-2], [0], [-3], [], [], [], []],
        [None, None, None, None, -3, None, 0, -2],
    )
])
def test_minStack(actions, args, expecteds):
    minStack = MinStack()

    for action, arg, expected in zip(
        actions[1:], args[1:], expecteds[1:]
    ):
        actual = getattr(minStack, action)(*arg)
        assert actual == expected
