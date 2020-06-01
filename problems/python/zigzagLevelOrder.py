from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, tmp, direction = [], [], 1
        q, next_q = [root], []

        while q or next_q:
            cur = q.pop(0)
            tmp.append(cur.val)
            if cur.left:
                next_q.append(cur.left)
            if cur.right:
                next_q.append(cur.right)

            if not q:
                q = next_q
                res.append(tmp[::direction])
                next_q, tmp, direction = [], [], direction*-1

        return res
