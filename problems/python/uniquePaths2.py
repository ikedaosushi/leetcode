class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0]:
            return 0
        
        obstacleGrid[0][0] = 1
        
        # 1列目を初期化
        for i in range(1, m):
            # 現在地に障害物がなくて1つ前まで来ている(1である)
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
    
        # 1行目を初期化
        for i in range(1, n):
            # 現在地に障害物がなくて1つ前まで来ている(1である)
            obstacleGrid[0][i] = int(obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1)
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
                    
                    
        return obstacleGrid[m-1][n-1]
    
#     Divide and Conque => Time exceeds
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         self.paths = 0
#         self._unqPath(0, 0, obstacleGrid)
#         return self.paths
        
#     def _unqPath(self, current_x, current_y, grid):
#         # print("current_x, current_y:", current_x, current_y)
#         if(grid[current_x][current_y] == 1):
#             return 
        
#         if(len(grid)-1 == current_x and len(grid[0])-1 == current_y):
#             self.paths += 1
#             return 
        
#         # right
#         if(len(grid)-1 > current_x):
#             # if grid[current_x+1][current_y] != 1:
#             self._unqPath(current_x+1, current_y, grid)
        
#         # down
#         if(len(grid[0])-1 > current_y):
#             # if grid[current_x][current_y+1] != 1:
#             self._unqPath(current_x, current_y+1, grid)