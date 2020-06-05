from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in hashmap and hashmap[rest] != i:
                return [i, hashmap[rest]]
