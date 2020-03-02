from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        while len(res) <= num:
            res += [i + 1 for i in res]

        return res[:num + 1]
