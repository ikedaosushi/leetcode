from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        subset = []
        # self.res.append(subset)
        self._subsets(nums, subset)
        return self.res

    def _subsets(self, nums: List[int], subset: List[int]):
        # print("[start] nums:", nums, ", subset: ", subset)
        self.res.append(subset)
        if len(nums) == 0:
            # print("return nums:", nums)
            return

        # print("res: ", self.res)
        for i in range(0, len(nums)):
            # print("nums:", nums, ", i: ", i)
            self._subsets(nums[i + 1:], subset + [nums[i]])
        # print("[end]")


if __name__ == "__main__":
    nums = [1, 2, 3]
    actual = Solution().subsets(nums)
    print("actual: ", actual)
