class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0

        for c in s:
            if c.isdigit():
                current_num = current_num * 10 + int(c)
            elif c == "[":
                stack.append(current_num)
                stack.append(current_string)
                current_string = ""
                current_num = 0
            elif c == "]":
                prev_string = stack.pop()
                prev_num = stack.pop()
                current_string = prev_string + prev_num * current_string
            else:
                current_string += c

        return current_string
