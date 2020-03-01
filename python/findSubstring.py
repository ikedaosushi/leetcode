from typing import List
from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        count = Counter(words)
        n, n_word = len(s), len(words[0])
        n_total = n_word * len(words)
        idxes = []

        for i in range(n - n_total + 1):
            seen = defaultdict(int)
            for j in range(i, i + n_total, n_word):
                current = s[j:j + n_word]
                if current in count:
                    seen[current] += 1
                    if seen[current] > count[current]:
                        break
                else:
                    break
            if seen == count:
                idxes.append(i)

        return idxes
