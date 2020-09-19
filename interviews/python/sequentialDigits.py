from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for d in range(1, 9):
            num = next_ = d
            while num <= high and next_ < 10:
                if num >= low:
                    ans.append(num)
                next_ += 1
                num = num * 10 + next_
        return sorted(ans)
