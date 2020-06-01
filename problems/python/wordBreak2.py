from typing import List, Dict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self._wordBreak(s, wordDict, memo={})

    def _wordBreak(self, s: str, wordDict: List[str], memo: Dict[str, List[str]]) -> List[str]:
        if not s:
            return []
        if s in memo:
            return memo[s]

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            elif len(s) == len(word):
                res.append(word)
            else:
                rest = self._wordBreak(s[len(word):], wordDict, memo)
                for r in rest:
                    res.append(f"{word} {r}")
        memo[s] = res

        return res
