class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mapping = {
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
        }

        num1_int = 0
        num2_int = 0

        num1 = list(num1)
        num2 = list(num2)

        i = 0
        while True:
            if num1:
                num1_int +=  mapping[num1.pop()] * (10**(i))
            else:
                break
            i += 1

        i = 0
        while True:
            if num2:
                num2_int +=  mapping[num2.pop()] * (10**(i))
            else:
                break
            i += 1

        mul = num1_int * num2_int
        # print(num1_int, num2_int, mul)

        mapping = {v: k for k, v in mapping.items()}
        res = ""

        while True:
            mul, mod = divmod(mul, 10)
            # print(mul, mod, mapping[mod], res)
            res = mapping[mod] + res
            if mul == 0:
                break

        return res