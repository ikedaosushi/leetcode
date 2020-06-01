class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0

        return 1 + max(self._dfs(node.left), self._dfs(node.right))

    def maxDepth(self, root: TreeNode) -> int:
        return self._dfs(root)
