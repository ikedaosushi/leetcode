from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = {str(cells): N}
        while N:
            N -= 1
            cells = [0] + [cells[i-1] ^ cells[i+1]
                           ^ 1 for i in range(1, 7)] + [0]
            if str(cells) if seen:
                N %= seen[str(cells)] - N

        return cells
