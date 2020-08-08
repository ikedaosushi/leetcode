
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.dfs(root, sum)
        return self.res

    def dfs(self, root, value):
        if not root:
            return

        self.test(root, value)
        self.pathSum(root.left, value)
        self.pathSum(root.right, value)

    def test(self, node, value):
        if not node:
            return

        if node.val == value:
            self.res += 1

        self.test(node.left, value - node.val)
        self.test(node.right, value - node.val)
