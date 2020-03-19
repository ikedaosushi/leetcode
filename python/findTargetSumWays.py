from typing import List

class Solution:
    def dfs(self, current_sum, nums, S):
        if (len(nums), current_sum) in self.memo:
            return self.memo[(len(nums), current_sum)]

        if len(nums) == 0:
            if current_sum == S:
                return 1
            else:
                return 0
        pos = self.dfs(current_sum + nums[0], nums[1:], S)
        neg = self.dfs(current_sum - nums[0], nums[1:], S)
        res = pos + neg
        self.memo[(len(nums), current_sum)] = res

        return res
        
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.memo = {}
        return self.dfs(0, nums, S)