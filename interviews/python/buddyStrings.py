from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        counter_a, counter_b = Counter(A), Counter(B)
        if counter_a != counter_b:
            return False

        diff = sum(i != j for i, j in zip(A, B))

        if diff not in [0, 2]:
            return False

        if diff == 0 and len(counter_a) == len(A):
            return False

        if diff == 2 and len(counter_a) == 1:
            return False

        return True
