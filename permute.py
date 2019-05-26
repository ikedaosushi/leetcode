class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self._permute(nums, [], res)
        return res
        
    def _permute(self, nums, combi, res):
        if len(nums) == 0:
            res.append(combi)
            return
        
        for i in range(len(nums)):
            _nums = nums[:]
            val = _nums.pop(i)
            self._permute(_nums, combi+[val], res)