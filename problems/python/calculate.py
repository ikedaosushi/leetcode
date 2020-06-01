class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack, num, op = [], 0, "+"

        def calc_ops(stack, op, num):
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(int(stack.pop() * num))
            else:
                stack.append(int(stack.pop() / num))

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                calc_ops(stack, op, num)
                op = c
                num = 0

        calc_ops(stack, op, num)

        return sum(stack)
