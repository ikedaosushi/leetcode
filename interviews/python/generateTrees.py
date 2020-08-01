from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self._gen(1, n)

    def _gen(self, first, last):
        return [
            TreeNode(root, left, right)
            for root in range(first, last + 1)
            for left in self._gen(first, root-1)
            for right in self._gen(root+1, last)
        ] or [None]
