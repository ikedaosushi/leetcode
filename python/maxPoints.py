from typing import List


class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def frac(self, x, y):
        g = self.gcd(x, y)
        return x // g, y // g

    def maxPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        m = 0
        for i in range(l):
            dic = dict(i=1)
            same = 0
            for j in range(i+1, l):
                tx, ty = points[j][0], points[j][1]
                dx = points[i][0] - tx
                dy = points[i][1] - ty

                if tx == points[i][0] and ty == points[i][1]:
                    same += 1
                    continue
                if dx == 0:
                    slope = 'i'
                else:
                    slope = self.frac(dx, dy)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)

        return m
