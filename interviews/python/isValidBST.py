class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._isValidBST(root, float("-inf"), float("inf"))

    def _isValidBST(self, node, min_, max_):
        if node is None:
            return True
        if not (min_ < node.val < max_):
            return False

        return self.isValidBST(self.left, min_, node.val) and self.isValidBST(self.right, node.val, max_)
