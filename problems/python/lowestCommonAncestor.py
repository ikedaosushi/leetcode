class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _lca(self, current, p, q) -> TreeNode:
        if current in [None, p, q]:
            return current
        left = self._lca(current.left, p, q)
        right = self._lca(current.right, p, q)

        return current if left and right else left or right

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self._lca(root, p, q)
