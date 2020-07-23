class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def helper(curr):
            if curr is None:
                return False

            mid = curr is p or curr is q
            left = helper(curr.left)
            right = helper(curr.right)

            if mid + left + right == 2:
                self.ans = curr

            return mid or left or right
        helper(root)

        return self.ans
