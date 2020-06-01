class Solution:
    def canJump(self, nums):
        j = 0
        for i, x in enumerate(nums):
            if j < i: return False
            j = max(j, i+x)
        return True

#     Time exceeed limit
#     def canJump(self, nums: List[int]) -> bool:
#         memo = ["unkown" for _ in nums]
#         memo[-1] = "good"
#         return self.canJumpFromPosition(0, nums, memo)

#     def canJumpFromPosition(self, pos, nums, memo) -> bool:
#         if memo[pos] != "unkown":
#             if memo[pos] == "good":
#                 return True
#             else:
#                 return False

#         furthest = min(pos + nums[pos], len(nums)-1)

#         next_ = pos + 1
#         while next_ <= furthest:
#             if (self.canJumpFromPosition(next_, nums, memo)):
#                 memo[pos] = "good"
#                 return True
#             next_ += 1

#         memo[pos] = "bad"
#         return False