# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return str([])
        res = []
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr is not None:
                res.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                res.append("null")

        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        null2None = {"null": None}
        nums = [null2None.get(num, num) for num in eval(data)]
        if len(nums) < 1:
            return None

        root = TreeNode(nums[0])
        queue = [root]
        idx = 1
        while queue:
            try:
                current = queue.pop(0)
                if nums[idx] is not None:
                    left = TreeNode(nums[idx])
                    current.left = left
                    queue.append(left)
                idx += 1
                if nums[idx] is not None:
                    right = TreeNode(nums[idx])
                    current.right = right
                    queue.append(right)
                idx += 1
            except IndexError:
                break

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
