from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr is None:
                continue
            res.append(curr.val)
            stack.append(curr.left)
            stack.append(curr.right)

        return reversed(res)
