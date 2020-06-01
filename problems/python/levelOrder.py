from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        vals = []
        current_vals = []
        current_queue = [root]
        next_queue = []
        while current_queue or next_queue:
            if not current_queue:
                current_queue = [*next_queue]
                next_queue = []
                vals.append(current_vals)
                current_vals = []

            current = current_queue.pop(0)
            current_vals.append(current.val)
            if current.left:
                next_queue.append(current.left)
            if current.right:
                next_queue.append(current.right)
        vals.append(current_vals)

        return vals


if __name__ == "__main__":
    from utils.binary_tree import from_nums
    nums = [3, 9, 20, None, None, 15, 7]
    root = from_nums(nums)
    vals = Solution().levelOrder(root)
    print(vals)
