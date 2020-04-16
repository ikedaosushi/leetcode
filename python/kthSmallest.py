from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result, heap = None, []
        heapq.heappush(heap, (matrix[0][0], 0, 0))

        while k > 0:
            result, i, j = heapq.heappop(heap)
            print(heap, result, i, j, result)
            if i == 0 and j < len(matrix) - 1:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
            if i < len(matrix) - 1:
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            k -= 1

        return result


if __name__ == "__main__":
    matrix, k = [
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ], 8
    Solution().kthSmallest(matrix, k)
