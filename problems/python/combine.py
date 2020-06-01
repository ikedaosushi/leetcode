from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.cmbs = []
        self.array_length = n
        self.cmb_length = k
        self._combine(1, [])

        return self.cmbs

    def _combine(self, idx, tmp_cmb):
        rest = self.cmb_length - len(tmp_cmb)
        # print("tmp_cmb:", tmp_cmb)
        # print("rest:", rest)
        if rest == 0:
            self.cmbs.append(tmp_cmb)
            return
        for new_idx in range(idx, (self.array_length - rest + 1) + 1):
            # print("new_idx:", new_idx)
            self._combine(new_idx + 1, tmp_cmb + [new_idx])


if __name__ == "__main__":
    n, k = 4, 2
    actual = Solution().combine(n, k)
    expected = [[a, b] for a, b in combinations(range(1, n + 1), k)]
    print(actual)
    print(expected)
