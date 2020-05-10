from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            try:
                t = int(t)
                stack.append(t)
            except:
                second = stack.pop()
                first = stack.pop()
                if t == "+":
                    tmp = first + second
                if t == "-":
                    tmp = first - second
                if t == "*":
                    tmp = first * second
                if t == "/":
                    tmp = int(first / second)

                stack.append(tmp)

        return stack[-1]
