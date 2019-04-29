class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        
        def backtrace(combi_str, rest_digits):
            if len(rest_digits) == 0:
                output.append(combi_str)
            else:
                next_digit = rest_digits[0]
                next_strs = digit_map[next_digit]
                for lune in next_strs:
                    backtrace(combi_str + lune, rest_digits[1:])
        
        output = []
        
        if digits:
            backtrace("", digits)
        
        return output