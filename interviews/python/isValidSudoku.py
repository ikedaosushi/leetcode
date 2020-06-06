from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                tmp = board[i][j]
                if tmp == ".":
                    continue
                if tmp in rows.get(i, {}):
                    return False
                if tmp in cols.get(j, {}):
                    return False
                if tmp in boxes.get((i // 3, j // 3), {}):
                    return False

                rows[i].add(tmp)
                cols[j].add(tmp)
                boxes[(i // 3, j // 3)].add(tmp)

        return True
