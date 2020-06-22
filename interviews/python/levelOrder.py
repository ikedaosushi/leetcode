from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        next_q = []
        res = [[n.val for n in queue]]
        while queue or next_q:
            current = queue.pop(0)
            if current.left:
                next_q.append(current.left)
            if current.right:
                next_q.append(current.right)

            if len(queue) == 0:
                res.append([n.val for n in next_q])
                queue = next_q

        return res
