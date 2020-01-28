class Solution:
    def myAtoi(self, s: str) -> int:
        minus = None
        res = 0
        found = False
        for c in s:
            if not found and c == " ":
                continue

            if found and c in ("+", "-"):
                break

            if c != " ":
                found = True
            if c == "-":
                minus = True
            elif c == "+":
                minus = False
            elif not c.isdigit():
                break

            else:
                res = res * 10 + int(c)

        if minus:
            res = res * -1

        if res >= 2 ** 31:
            res = 2 ** 31 - 1

        elif res < - 2 ** 31:
            res = - 2 ** 31

        return res
