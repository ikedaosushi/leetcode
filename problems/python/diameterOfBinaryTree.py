class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def depth(self, node: TreeNode):
        if node is None:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter
