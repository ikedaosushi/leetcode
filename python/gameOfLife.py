from typing import List


class Solution:
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0),
                 (-1, -1), (1, 1), (-1, 1), (1, -1)]

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                count = self._count(board, m, n, i, j)
                if board[i][j] == 1 and count < 2:
                    board[i][j] = 3
                elif board[i][j] == 1 and count in (2, 3):
                    board[i][j] = 1
                elif board[i][j] == 1 and count > 3:
                    board[i][j] = 3
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

    def _count(self, board, m, n, i, j):
        count = 0
        for d in self.neighbors:
            if 0 <= i + d[0] < m and 0 <= j + d[1] < n:
                count += board[i+d[0]][j+d[1]] % 2

        return count
