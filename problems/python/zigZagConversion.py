class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        
        rows = ["" for _ in range(min(numRows, len(s)))]
        row = 0
        down = False
        
        for c in s:
            rows[row] += c
            if row == 0 or row == (numRows-1):
                down = not down
            row = row + 1 if down else row - 1
            
        ret = "".join(rows)
        
        return ret
            
        
    def convert_slow(self, s: str, numRows: int) -> str:
        arr = [[""] for _ in range(numRows)]
        x, y = 0, 0
        x_dir = 0
        y_dir = 1
        
        if numRows <= 1:
            return s
        
        for i, s_ in enumerate(s):
            if (i > 0) and (i % (numRows-1) == 0):
                x_dir = 1 if x_dir == 0 else 0
                y_dir = -1 if y_dir == 1 else 1
                for a in arr:
                    a.extend([""] * (max(numRows-2, 1)))
            # print("i", i, "x", x, "y", y)
            # print("arr", arr)
            arr[y][x] = s_
            
            x = x + x_dir
            y = y + y_dir
        
        resl = "".join(["".join(a) for a in arr])
        
        return resl