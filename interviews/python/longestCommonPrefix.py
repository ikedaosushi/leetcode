from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        min_len = min(len(s) for s in strs)
        for idx in range(min_len):
            base = strs[0][idx]
            for s in strs[1:]:
                if base != s[idx]:
                    return res

            res += base

        return res
