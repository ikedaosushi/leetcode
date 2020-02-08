from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self._sm(matrix, 0, 0, target)

    def _sm(self, matrix, i, j, target):
        if len(matrix) - 1 < i or len(matrix[0]) - 1 < j or matrix[i][j] is None or matrix[i][j] > target:
            return False

        if matrix[i][j] == target:
            return True

        res = self._sm(matrix, i + 1, j, target) or self._sm(matrix, i, j + 1, target)
        if not res:
            matrix[i][j] = None
        return res


if __name__ == "__main__":
    matrix, target = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 20

    actual = Solution().searchMatrix(matrix, target)
    print(actual)
