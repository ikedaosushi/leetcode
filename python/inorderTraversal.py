from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, res: List[int], node: TreeNode):
        if node.left:
            self.dfs(res, node.left)
        res.append(node.val)
        if node.right:
            self.dfs(res, node.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        self.dfs(res, root)
        return res
