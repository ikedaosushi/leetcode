from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = int("".join([str(d) for d in digits]))
        digit += 1
        digits = [int(d) for d in list(str(digit))]

        return digits
