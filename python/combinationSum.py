class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, current_idx, path, res):
        if target < 0:
            return

        if target == 0:
            res.append(path)
            return

        for next_idx in range(current_idx, len(nums)):
            next_value = nums[next_idx]
            self.dfs(nums, target - next_value, next_idx, path + [next_value], res)
