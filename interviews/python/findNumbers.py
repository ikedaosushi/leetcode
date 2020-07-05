from typing import List
import math


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(int(math.log10(num)) % 2 for num in nums)
