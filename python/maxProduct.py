from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = small = big = nums[0]

        print("n:", nums[0], "small:", small, "big:", big, "res:", res)
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            res = max(res, big, small)
            print("n:", n, "small:", small, "big:", big, "res:", res)

        return res


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print("nums:", nums)
    actual = Solution().maxProduct(nums)

    print()
    nums = [2, 3, -2, 4, 5, 8]
    print("nums:", nums)
    actual = Solution().maxProduct(nums)

    print()
    nums = [-4, -3, -2]
    print("nums:", nums)
    actual = Solution().maxProduct(nums)
