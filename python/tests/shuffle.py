from typing import List
from random import randint
from copy import deepcopy


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = deepcopy(self.nums)
        for i in range(len(self.nums)):
            j = randint(0, len(nums) - 1)
            nums[i], nums[j] = nums[j], nums[i]

        return nums
