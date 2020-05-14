from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(set)
        neigh = defaultdict(set)

        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)

        stack = [i for i in range(numCourses) if not dic[i]]
        res = []

        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)

            dic.pop(node)

        return res if not dic else []
