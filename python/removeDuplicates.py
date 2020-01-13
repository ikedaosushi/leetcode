from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = None
        count = 0
        i = 0
        while i < len(nums):
            # print("i:", i, "nums:", nums, "tmp:", tmp, "nums[i]:", nums[i], "count:", count)
            if tmp == nums[i]:
                count += 1
                if count >= 2:
                    # print("count:", count)
                    nums.pop(i)
                    i -= 1
            else:
                count = 0
            tmp = nums[i]
            i += 1

        return len(nums)


if __name__ == "__main__":
    nums, expected = ([1, 1, 1, 2, 2, 3, 3, 3, 3], [1, 1, 2, 2, 3, 3])
    length = Solution().removeDuplicates(nums)
    print(nums)
