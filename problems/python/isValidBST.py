class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, node: TreeNode, larger_than=float('-inf'), less_than=float("inf")):
        if node is None:
            return True

        if not (larger_than < node.val < less_than):
            return False

        return self.dfs(node.left, larger_than, node.val) and self.dfs(node.right, node.val, less_than)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root)
