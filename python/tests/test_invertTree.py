import pytest
from queue import Queue
from invertTree import Solution


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


@pytest.mark.parametrize("nums,expected", [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([], [])
])
def test_invertTree(nums, expected):
    if len(nums) == 0:
        assert Solution().invertTree(None) is None
        return

    q = Queue()
    root = TreeNode(nums[0])
    q.put(root)
    for left, right in zip(*[iter(nums[1:])] * 2):
        current = q.get()
        current.left = TreeNode(left)
        current.right = TreeNode(right)
        q.put(current.left)
        q.put(current.right)

    actual_node = Solution().invertTree(root)

    actual = []
    q = Queue()
    q.put(actual_node)
    while not q.empty():
        current = q.get()
        actual.append(current.val)
        if current.left:
            q.put(current.left)
        if current.right:
            q.put(current.right)
    assert actual == expected
