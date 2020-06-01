class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, node):
        if node is None:
            return None
        self.dfs(node.right)
        self.dfs(node.left)

        node.right = self.prev
        node.left = None
        self.prev = node

    def flatten(self, root: TreeNode) -> None:
        self.prev = None
        self.dfs(root)
