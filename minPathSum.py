class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # DPで解く
        m = len(grid)
        n = len(grid[0])
        
        # 1行目を足す
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        # 1列目を足す
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        # 2行目2列目以降を足していく
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                
        return grid[-1][-1]