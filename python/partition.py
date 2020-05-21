from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return

        for i in range(1, len(s) + 1):
            cur = s[:i]
            if cur == cur[::-1]:
                self.dfs(s[i:], path + [cur], res)
