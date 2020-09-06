class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.res = 0
        self.dfs(root, "")
        return self.res

    def dfs(self, node: TreeNode, val):
        val += str(node.val)
        if node.left is None and node.right is None:
            self.res += int(val, 2)
        if node.left:
            self.dfs(node.left, val)
        if node.right:
            self.dfs(node.right, val)
