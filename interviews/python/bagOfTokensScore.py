import collections
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        res = cur = 0
        d = collections.deque(sorted(tokens))
        while d and (d[0] <= P or cur):
            if d[0] <= P:
                P -= d.popleft()
                cur += 1
            else:
                P += d.pop()
                cur -= 1
            res = max(res, cur)
        return res
