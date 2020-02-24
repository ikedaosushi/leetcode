class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        left_queue = [root]
        right_queue = [root]
        left_nums = []
        right_nums = []

        while left_queue:
            left_current = left_queue.pop(0)
            right_current = right_queue.pop(0)
            if left_current:
                left_nums.append(left_current.val)
                left_queue.append(left_current.left)
                left_queue.append(left_current.right)
            else:
                left_nums.append(None)

            if right_current:
                right_nums.append(right_current.val)
                right_queue.append(right_current.right)
                right_queue.append(right_current.left)
            else:
                right_nums.append(None)

        print("left:", left_nums)
        print("right:", right_nums)

        return left_nums == right_nums


if __name__ == "__main__":
    nums = [1, 2, 2, None, 3, None, 3]
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
    Solution().isSymmetric(root)
