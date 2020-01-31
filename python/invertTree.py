from queue import Queue

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        queue = []
        queue.insert(0, root)
        while len(queue):
            current = queue.pop()
            current.left, current.right = current.right, current.left
            if current.left:
                queue.insert(0, current.left)
            if current.right:
                queue.insert(0, current.right)

        return root


if __name__ == "__main__":
    nums = [4, 2, 7, 1, 3, 6, 9]
    q = Queue()
    root = TreeNode(nums[0])
    q.put(root)
    for left, right in zip(*[iter(nums[1:])] * 2):
        current = q.get()
        current.left = TreeNode(left)
        current.right = TreeNode(right)
        q.put(current.left)
        q.put(current.right)

    actual = Solution().invertTree(root)

    q = Queue()
    q.put(actual)
    while not q.empty():
        current = q.get()
        print(current.val)
        if current.left:
            q.put(current.left)
        if current.right:
            q.put(current.right)
