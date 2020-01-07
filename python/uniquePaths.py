class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        aux = [[1 for _ in range(n)] for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1] + aux[i-1][j]
        
        return aux[m-1][n-1]