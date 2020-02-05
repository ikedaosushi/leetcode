import pytest
from queue import Queue
from lowestCommonAncestor import Solution


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


@pytest.mark.parametrize("nums,p_val,q_val,expected_val", [
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5)
])
def test_lowestCommonAncestor(nums, p_val, q_val, expected_val):
    if len(nums) == 0:
        assert Solution().lowestCommonAncestor(None) is None
        return

    q = Queue()
    root = TreeNode(nums[0])
    q.put(root)
    nodes = [root]
    for left, right in zip(*[iter(nums[1:])] * 2):
        current = q.get()
        current.left = TreeNode(left)
        current.right = TreeNode(right)
        q.put(current.left)
        q.put(current.right)
        nodes.append(current.left)
        nodes.append(current.right)

    for n in nodes:
        if n.val == p_val:
            p = n
        if n.val == q_val:
            q = n
        if n.val == expected_val:
            expected = n

    actual = Solution().lowestCommonAncestor(root, p, q)

    assert actual.val == expected.val
