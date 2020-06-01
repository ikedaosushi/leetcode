class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _maxPathSum(self, node: TreeNode) -> [int, int]:
        if node is None:
            return [-2**31, -2**31]
        left_max = self._maxPathSum(node.left)
        right_max = self._maxPathSum(node.right)
        current_max = node.val + max(left_max[0], right_max[0], 0)

        print(
            f"current: {node.val}, curent_max: {current_max}, left_max: {left_max}, right_max: {right_max}")

        return [
            current_max,
            max(left_max + right_max + [node.val + left_max[0] + right_max[0]])
        ]

    def maxPathSum(self, root: TreeNode) -> int:
        return max(self._maxPathSum(root))
