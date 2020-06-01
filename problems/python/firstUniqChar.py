from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        only_once = {k for k, v in counter.items() if v == 1}
        if not only_once:
            return -1
        for idx, c in enumerate(s):
            if c in only_once:
                return idx
