class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.result = 0
        cache = {0: 1}

        self.dfs(root, target, cache, current_path_sum=0)

        return self.result

    def dfs(self, node, target, cache: int, current_path_sum: int):
        if node is None:
            return

        current_path_sum += node.val
        old_path_sum = current_path_sum - target
        self.result += cache.get(old_path_sum, 0)
        cache[current_path_sum] = cache.get(current_path_sum, 0) + 1

        self.dfs(node.left, target, cache, current_path_sum)
        self.dfs(node.right, target, cache, current_path_sum)

        cache[current_path_sum] -= 1
