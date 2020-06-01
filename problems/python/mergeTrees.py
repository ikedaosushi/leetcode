class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        head = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        head.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        head.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)

        return head
