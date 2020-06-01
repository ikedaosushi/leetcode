from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, i, j, word[1:]):
                    return True

        return False

    def dfs(self, board: List[List[str]], i: int, j: int, word: str) -> bool:
        if len(word) == 0:
            return True

        original, board[i][j] = board[i][j], "#"
        res = False

        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[0] and self.dfs(board, x, y, word[1:]):
                res = True
                break

        board[i][j] = original

        return res


if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    # word = "ABCCED"
    word = "SEE"
    actual = Solution().exist(board, word)
    print(actual)
