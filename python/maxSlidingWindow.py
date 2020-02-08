from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 1:
            return nums

        res = []
        deq = deque()

        for i in range(k):
            while len(deq) > 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        for i in range(k, len(nums)):
            res.append(nums[deq[0]])

            if deq[0] < i - k + 1:
                deq.popleft()

            while len(deq) > 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        # last sequence
        res.append(nums[deq[0]])

        return res

    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if len(nums) == 0:
    #         return []
    #     res = []
    #     for i in range(len(nums) - (k - 1)):
    #         res.append(max(nums[j] for j in range(i, i + k)))

    #     return res


if __name__ == "__main__":
    # nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    nums, k = [9, 11], 2
    actual = Solution().maxSlidingWindow(nums, k)
    print(actual)
