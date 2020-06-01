class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        
        R, C = len(matrix), len(matrix[0])
        
        seen = [[False for _ in range(C)] for _ in range(R)]
        
        ans = []
        
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        r = c = di = 0
        
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            tr, tc = r + dr[di], c + dc[di]
            
            if 0 <= tr < R and 0 <= tc < C and not seen[tr][tc]:
                r, c = tr, tc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
                
        return ans