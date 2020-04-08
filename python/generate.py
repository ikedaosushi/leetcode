from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for _ in range(1, numRows):
            res.append([x + y for x, y in zip(res[-1] + [0], [0] + res[-1])])

        return res
