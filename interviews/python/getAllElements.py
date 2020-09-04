from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def convertList(node: TreeNode, ls: List[int]):
            if node is None:
                return
            convertList(node.left, ls)
            ls.append(node.val)
            convertList(node.right, ls)

        list1 = []
        list2 = []
        convertList(root1, list1)
        convertList(root2, list2)

        ans = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                ans.append(list1[i])
                i += 1
            else:
                ans.append(list2[j])
                j += 1
        return ans + list1[i:] + list2[j:]
