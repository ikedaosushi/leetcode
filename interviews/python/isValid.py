class Solution:
    validCombi = {
        ")": "(", "]": "[",  "}": "{"
    }

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if len(stack) == 0 or self.validCombi[c] != stack.pop():
                    return False

        return len(stack) == 0
