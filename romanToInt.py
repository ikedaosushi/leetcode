class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1)
        ]
        ret = ""
        max_i = 0
        
        while True:
            for i, (sym, val) in enumerate(symbols[max(max_i-1, 0):]):
                # print("sym", sym, "val", val)
                if num - val >= 0:
                    num -= val
                    ret += sym
                    max_i = max(max_i, i)
                    break
                if num == 0:
                    break
            
            if num == 0:
                break
                   
        return ret
