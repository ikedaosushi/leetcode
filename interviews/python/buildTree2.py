from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inor_map = {}
        for i, n in enumerate(inorder):
            inor_map[n] = i
        pre_iter = iter(preorder)

        def helper(start, end):
            if start > end:
                return None

            root_val = next(pre_iter)
            root = TreeNode(root_val)
            idx = inor_map[root_val]
            root.left = helper(start, idx-1)
            root.right = helper(idx+1, end)
            return root

        return helper(0, len(inorder) - 1)
