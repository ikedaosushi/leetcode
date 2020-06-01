class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtrace(S, left, right):
            # return
            if len(S) == n * 2:
                answer.append(S)
                return

            if left < n:
                backtrace(S+"(", left+1, right)

            if right < left:
                backtrace(S+")", left, right+1)

        backtrace("", 0, 0)
        return answer