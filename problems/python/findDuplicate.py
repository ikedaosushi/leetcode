from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)

        while low < high:
            middle = int(low + (high - low) / 2)
            cnt = 0

            for n in nums:
                if n <= middle:
                    cnt += 1

            if cnt <= middle:
                low = middle + 1
            else:
                high = middle

        return low


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    Solution.findDuplicate(nums)
