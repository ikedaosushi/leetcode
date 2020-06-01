from typing import List
from collections import defaultdict


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        people_dic, res, height = defaultdict(list), [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] not in people_dic:
                height.append(p[0])
            people_dic[p[0]] += [(p[1], i)]

        height.sort()

        for h in height[::-1]:
            people_dic[h].sort()
            for p in people_dic[h]:
                res.insert(p[0], people[p[1]])

        return res
