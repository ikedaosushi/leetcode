from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append(i)

        return ans
