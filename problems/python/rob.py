from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _rob(self, node: Optional[TreeNode]):
        if not node:
            return (0, 0)

        left, right = self._rob(node.left), self._rob(node.right)

        now = node.val + left[1] + right[1]
        later = max(left) + max(right)

        return (now, later)

    def rob(self, root: TreeNode) -> int:
        return max(self._rob(root))
