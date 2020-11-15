class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return self.inorder(root, 0, low, high)

    def inorder(self, root, value, low, high):
        if root:
            value = self.inorder(root.left, value, low, high)
            if root.val >= low and root.val <= high:
                value += root.val
            value = self.inorder(root.right, value, low, high)

        return value
