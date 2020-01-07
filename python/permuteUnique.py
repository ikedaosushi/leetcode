from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def back_trace(path, counter):
            if len(path) == len(nums):
                ans.append(path[:])
            for x in counter:
                if counter[x] > 0:
                    path.append(x)
                    counter[x] -= 1
                    back_trace(path, counter)
                    path.pop()
                    counter[x] += 1
                    
        ans = []
        back_trace([], Counter(nums))
        return ans
