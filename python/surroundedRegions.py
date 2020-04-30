from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) == 0:
            return board
        m, n = len(board), len(board[0])
        queue = []
        for r in range(m):
            for c in range(n):
                if r in [0, m-1] or c in [0, n - 1] and board[r][c]:
                    queue.append((r, c))

        while queue:
            r, c = queue.pop(0)
            if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
                board[r][c] = "D"
                queue.extend([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "D":
                    board[r][c] = "O"
