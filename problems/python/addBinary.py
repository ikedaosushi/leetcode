class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print("a:", a, "b:", b)
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        if len(a) < len(b):
            a = [0] * (len(b) - len(a)) + a
        else:
            b = [0] * (len(a) - len(b)) + b
        print("a:", a, "b:", b)

        carry = 0
        res = []
        for i in range(1, len(a) + 1):
            tmp = carry + a[-i] + b[-i]
            print("tmp:", tmp)
            if tmp >= 2:
                tmp -= 2
                carry = 1
            else:
                carry = 0

            print("tmp:", tmp, "carry:", carry)

            res.insert(0, tmp)
        if carry == 1:
            res.insert(0, 1)

        return "".join([str(x) for x in res])


if __name__ == "__main__":
    a, b, expected = ("11110", "101", "100011")
    actual = Solution().addBinary(a, b)
    print(actual)
    print(expected)
