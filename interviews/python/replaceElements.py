from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        n = len(arr)
        while i < n - 1:
            max_ = 0
            max_j = 0
            for j in range(i+1, n):
                if max_ <= arr[j]:
                    max_ = arr[j]
                    max_j = j

            for k in range(i, max_j):
                arr[k] = max_
            i = max_j

        arr[-1] = -1
        return arr


if __name__ == "__main__":
    Solution().replaceElements([17, 18, 5, 4, 6, 1])
