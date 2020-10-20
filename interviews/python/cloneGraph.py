"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        m = {node: Node(node.val)}
        stack = [node]
        while stack:
            n = stack.pop()
            for neigh in n.neighbors:
                if neigh not in m:
                    stack.append(neigh)
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])

        return m[node]


#         if not node:
#             return node
#         m = {node: Node(node.val)}
#         stack = [node]
#         while stack:
#             n = stack.pop()
#             for neigh in n.neighbors:
#                 if neigh not in m:
#                     stack.append(neigh)
#                     m[neigh] = Node(neigh.val)
#                 m[n].neighbors.append(m[neigh])
#         return m[node]
