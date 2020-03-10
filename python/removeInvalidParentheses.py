from typing import List


class Solution:
    def isValid(self, s) -> bool:
        stack = 0
        for lune in s:
            if lune == "(":
                stack += 1
            elif lune == ")":
                stack -= 1
                if stack < 0:
                    return False
        return stack == 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        res = []
        visited = set()
        queue = []

        queue.append(s)
        visited.add(s)

        found = False

        while(queue):
            s = queue.pop(0)
            if self.isValid(s):
                res.append(s)
                found = True
            if found:
                continue

            for i in range(len(s)):
                if s[i] not in ("(", ")"):
                    continue

                t = s[:i] + s[i + 1:]

                if t not in visited:
                    queue.append(t)
                    visited.add(t)

        return res
