class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[-1]
        n = len(nums)
        nums.sort()
        for i in range(len(nums) - 1):
            start = i + 1
            end = -1
            
            while start < (n + end):
                sum_ = nums[i] + nums[start] + nums[end]
                if (sum_ - target) == 0:
                    return sum_
                elif (sum_ - target) > 0:
                    end -= 1
                else:
                    start += 1
                    
                if abs(sum_ - target) < abs(result - target):
                    result = sum_
                    
        return result
            
            