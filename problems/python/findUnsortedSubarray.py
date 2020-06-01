from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        begin, end, min_, max_ = -1, -2, nums[-1], nums[0]
        for i in range(len(nums)):
            if nums[i] < max_:
                end = i
            else:
                max_ = nums[i]
            
            if min_ < nums[-i - 1]:
                begin = len(nums) -i -1 
            else:
                min_ = nums[-i - 1]

        return end - begin + 1


        