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
                if validCombi[c] != stack.pop():
                    return False

        return len(stack) == 0
