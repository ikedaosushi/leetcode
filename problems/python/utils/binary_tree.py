from typing import List, Any


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def from_nums(nums: List[Any]) -> TreeNode:
    root = TreeNode(nums[0])
    queue = [root]
    idx = 1
    while queue:
        try:
            current = queue.pop(0)
            if nums[idx]:
                left = TreeNode(nums[idx])
                current.left = left
                queue.append(left)
            idx += 1
            if nums[idx]:
                right = TreeNode(nums[idx])
                current.right = right
                queue.append(right)
            idx += 1
        except IndexError:
            break

    return root
