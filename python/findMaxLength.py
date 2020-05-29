from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table = {0: 0}
        max_length = 0
        count = 0
        for i, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in table:
                max_length = max(max_length, i - table[count])
            else:
                table[count] = i

        return max_length
