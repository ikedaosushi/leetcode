from typing import List


class Solution:
    def setZeroes_(self, matrix: List[List[int]]) -> None:
        zeroRows = set()
        zeroCols = set()
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if n == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)
        for i in zeroRows:
            matrix[i] = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in zeroCols:
                matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        top_row_zero, top_col_zero = False, False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                top_row_zero = True

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                top_col_zero = True

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0] * len(matrix[0])

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

        if top_col_zero:
            matrix[0] = [0] * len(matrix[0])

        if top_row_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0


if __name__ == "__main__":
    matrix, expected = (
        [
            [1, 1, 1],
            [0, 1, 2]
        ],
        [
            [0, 1, 1],
            [0, 0, 0]
        ]
    )
    Solution().setZeroes(matrix)
