class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _kthSmallest(self, node, counts):
        if node is None:
            return

        self._kthSmallest(node.left, counts)
        counts.append(node.val)
        self._kthSmallest(node.right, counts)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        counts = []
        self._kthSmallest(root, counts)
        return counts[k-1]
